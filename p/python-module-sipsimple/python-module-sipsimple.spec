%define  modulename sipsimple
%def_enable bundled_pjsip

Name:    python-module-%modulename
Version: 3.1.1
Release: alt1

Summary: SIP SIMPLE implementation for Python
License: GPLv3
Group:   Development/Python
URL:     https://github.com/AGProjects/python-sipsimple

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-setuptools_cython
%if_enabled bundled_pjsip
BuildRequires: libavformat-devel
BuildRequires: libswscale-devel
BuildRequires: libvpx-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libv4l-devel
BuildRequires: libalsa-devel
%else
BuildRequires: libpjsip-devel
%endif

Source:  python-%modulename-%version.tar

%description
SIP SIMPLE client SDK is a Software Development Kit for easy development
of SIP end-points that support rich media like Audio, Video, Instant
Messaging, File Transfers, Desktop Sharing and Presence.  Other media
types can be easily added by using an extensible high-level API.

%prep
%setup -n python-%modulename-%version
chmod +x deps/pjsip/*configure

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
