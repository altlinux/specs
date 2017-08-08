
Name: yarn
Version: 0.27.5
Release: alt1%ubt
Summary: Fast, reliable, and secure dependency management
Group: Development/Tools
License: BSD
Url: https://yarnpkg.com
Source: https://github.com/yarnpkg/yarn/releases/download/v%version/yarn-v%version.tar.gz

BuildRequires(pre): rpm-macros-nodejs rpm-build-ubt

BuildArch: noarch

%description
Fast, reliable, and secure dependency management.
Yarn: Fast, reliable, and secure dependency management.

%prep
%setup -n dist

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%name %buildroot%_bindir
cp -a . %buildroot%nodejs_sitelib/%name/
ln -s %nodejs_sitelib/%name/bin/%name.js %buildroot%_bindir/%name
ln -s %nodejs_sitelib/%name/bin/%name.js %buildroot%_bindir/yarnpkg

%files
%_bindir/*
%nodejs_sitelib/%name

%changelog
* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 0.27.5-alt1%ubt
- rebuild with Universal Branch Tag

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 0.27.5-alt1
- first build for ALT Linux.
