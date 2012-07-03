Name: ofed-docs
Version: 1.5.2
Release: alt1.qa1
License: GPL/BSD
Url: https://openib.org/svn/gen2/branches/1.1/ofed/docs
Group: Documentation
Source: %{name}-%{version}.tar
Summary: OFED docs
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch

%description
OpenFabrics documentation

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
cp -a * $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%files
%{_defaultdocdir}/%{name}-%{version}

%changelog
* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.5.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * vendor-tag for ofed-docs

* Wed Dec 22 2010 Timur Aitov <timonbl4@altlinux.org> 1.5.2-alt1
- New OFED

* Thu Aug 19 2010 Andriy Stepanov <stanv@altlinux.ru> 1.5.1-alt1
- New OFED
