%define pname grunt

Name: node-grunt
Version: 1.4.1
Release: alt1

Summary: Grunt is a JavaScript library used for automation and running tasks

License: MIT
Group: Development/Other
Url: https://github.com/gruntjs/grunt

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/gruntjs/grunt/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

Provides: npm(%pname) = %version
#AutoReq: no
AutoProv: no

%description
Grunt is the JavaScript task runner. Why use a task runner? In one word:
automation. The less work you have to do when performing repetitive tasks
like minification, compilation, unit testing, linting, etc, the easier
your job becomes. After you've configured it, a task runner can do most
of that mundane work for you with basically zero effort.

%prep
%setup -a 1

%build
%npm_build
npm test --force
npm prune --production

%install
%npm_install
#mkdir -p %buildroot%_bindir
#ln -sr %buildroot%nodejs_sitelib/%pname/bin/grunt %buildroot%_bindir/grunt
cp -a node_modules %buildroot/%nodejs_sitelib/%pname/
# TODO: remove all test subdir
rm -rf %buildroot/%nodejs_sitelib/%pname/test/
rm -rf %buildroot/%nodejs_sitelib/%pname/node_modules/resolve/test/

%files
%doc LICENSE README.md
#%_bindir/grunt
%nodejs_sitelib/%pname/

%changelog
* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Tue Mar 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- initial build for ALT Sisyphus
