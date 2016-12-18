Name: gyp
Version: 0.1.g940a15e
Release: alt2

Summary: Generate Your Projects
License: BSD
Group: Development/Tools

Url: http://code.google.com/p/gyp/

BuildArch: noarch

# Source-git: https://chromium.googlesource.com/external/gyp
Source: %name-%version.tar
Patch: gyp-precompiled.patch

BuildRequires: python-module-setuptools python-devel

%add_python_req_skip TestCommon

%description
GYP is a tool to generates native Visual Studio, Xcode and SCons and/or
make  build files from a platform-independent input format. Its syntax
is a universal cross-platform build representation that still allows
sufficient per-platform flexibility to accommodate irreconcilable
differences.

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%python_sitelibdir/%name
%python_sitelibdir/%name-0.1-*
%doc AUTHORS LICENSE

%changelog
* Sun Dec 11 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.g940a15e-alt2
- add cmake_precompiled_header support from tdesktop project patch

* Sun Dec 11 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.g940a15e-alt1
- build lastest commit from git

* Sat Jun 16 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.1-alt1.r1415
- Update to SVN r1415

* Tue Mar 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.r1241
- initial build for Sisyphus

