%global _unpackaged_files_terminate_build 1

%define oname bootstrap

Name: javascript-%oname
Summary: HTML, CSS and JS framework
Version: 5.3.8
Release: alt1
License: MIT
Group: Development/Other
Url: https://getbootstrap.com/
Source: %name-%version.tar
# Patch: %%name-%%version.patch
BuildArch: noarch
Provides: libjs-%oname = %EVR

Requires: javascript-common
BuildRequires(pre): rpm-macros-javascript

%description
Bootstrap is a popular HTML, CSS, and JS framework for developing
responsive, mobile first projects on the web.
It includes base CSS and HTML for typography, forms, buttons, tables,
grids, navigation, and more.


%prep
%setup
# %%patch -p1

%build
%install
mkdir -p %buildroot%_jsdir/%oname
cp -p -r css %buildroot%_jsdir/%oname
cp -p -r js %buildroot%_jsdir/%oname

%files
%_jsdir/%oname


%changelog
* Wed Sep 03 2025 Sergey Konev <darisishe@altlinux.org> 5.3.8-alt1
- 5.3.8

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 3.4.1-alt2
- NMU: do not use deprecated rpm-macros-fontpackages

* Tue Jan 25 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.1-alt1
- Initial build.
