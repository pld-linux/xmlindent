Summary:	xmlindent - XML stream reformatter
Summary(pl):	xmlindent - reformater strumieni XML
Name:		xmlindent
Version:	0.2.17
Release:	2
License:	GPL v2
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/xmlindent/%{name}-%{version}.tar.gz
# Source0-md5:	c08be3867ee906ca69b949d55a4f3780
Source1:	%{name}.pl.1
# Source1-md5:	8e5a48ae48a6d3e62556058a0e86e1ce
URL:		http://xmlindent.sourceforge.net/
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id- u -n)

%description
xmlindent is a XML stream reformatter written in ANSI C.

%description -l pl
xmlindent jest programem napisanym w ANSI C przeformatowuj±cym
strumienie XML.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/xmlindent.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/pl/man1/*
