Summary:	xmlindent - XML stream reformatter
Summary(pl):	xmlindent - reformator strumieni XML
Name:		xmlindent
Version:	0.2.17
Release:	1
License:	GPL v2
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/xmlindent/%{name}-%{version}.tar.gz
# Source0-md5:	c08be3867ee906ca69b949d55a4f3780
URL:		http://xmlindent.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id- u -n)

%description
xmlindent is a XML stream reformatter written in ANSI C.

%description -l pl
xmlindent jest programem napisanym w ANSI C przeformatowuj±cym
strumienie XML.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install xmlindent $RPM_BUILD_ROOT%{_bindir}
install xmlindent.1 $RPM_BUILD_ROOT%{_mandir}/man1/xmlindent.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
