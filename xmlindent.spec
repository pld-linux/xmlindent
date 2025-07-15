Summary:	xmlindent - XML stream reformatter
Summary(pl.UTF-8):	xmlindent - reformater strumieni XML
Name:		xmlindent
Version:	0.2.17
Release:	3
License:	GPL v2
Group:		Applications/Publishing/XML
Source0:	http://downloads.sourceforge.net/xmlindent/%{name}-%{version}.tar.gz
# Source0-md5:	c08be3867ee906ca69b949d55a4f3780
Source1:	%{name}.pl.1
URL:		http://xmlindent.sourceforge.net/
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-Makefile.patch
BuildRequires:	flex
BuildRequires:	m4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmlindent is a XML stream reformatter written in ANSI C.

%description -l pl.UTF-8
xmlindent jest programem napisanym w ANSI C przeformatowującym
strumienie XML.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/xmlindent.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README
%attr(755,root,root) %{_bindir}/xmlindent
%{_mandir}/man1/xmlindent.1*
%lang(pl) %{_mandir}/pl/man1/xmlindent.1*
