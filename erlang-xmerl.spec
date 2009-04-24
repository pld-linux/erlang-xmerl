Summary:	Functions for exporting XML data to an external format
Name:		erlang-xmerl
Version:	0.20
Release:	1
License:	EPL 1.0
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/sowap/xmerl-%{version}.tar.gz
# Source0-md5:	edafb0316dd7cb0834e55ce78b7d9e84
URL:		http://sourceforge.net/projects/sowap/
BuildRequires:	erlang
Requires:	erlang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functions for exporting XML data to an external format.

%prep
%setup -q -n xmerl-%{version}

%build
%{__make} -C src

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/xmerl-%{version}
cp -a ebin src inc $RPM_BUILD_ROOT%{_libdir}/erlang/lib/xmerl-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.txt doc/*
%{_libdir}/erlang/lib/xmerl-*
