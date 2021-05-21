# This spec is backported to ALTLinux p8 automatically by rpmbph script from etersoft-build-utils.
#
%define  modulename crossbar

Name:    python3-module-%modulename
Version: 21.3.1
Release: alt1

Summary: Crossbar.io - WAMP application router
License: CC-BY-SA-3.0
Group:   Development/Python3
URL:     https://github.com/crossbario/crossbar

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%add_python3_req_skip crossbar.bridge.mqtt_events kjcbdkfbsdonfvspdmcsnofsn
%py3_requires watchdog ubjson cbor umsgpack lmdb sdnotify mistune passlib netaddr

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

echo '' > requirements-min.txt

%build
%python3_build

%install
%python3_install

rm -fr %buildroot%python3_sitelibdir/%modulename/worker/test/examples/syntaxerror.py

rm -fr %buildroot%prefix/COPYRIGHT
rm -fr %buildroot%prefix/LICENSE*

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed May 19 2021 Anton Midyukov <antohami@altlinux.org> 21.3.1-alt1
- new version 21.3.1

* Mon Aug 27 2018 Anton Midyukov <antohami@altlinux.org> 18.7.2-alt0.M80P.1
- backport to ALTLinux p8 (by rpmbph script)

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 18.7.2-alt1
- Initial build for Sisyphus
