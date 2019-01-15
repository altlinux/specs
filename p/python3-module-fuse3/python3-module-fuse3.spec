%define  origname pyfuse3
%define  modulename fuse3

Summary: Python 3 bindings for libfuse 3 with asynchronous API (Trio compatible)
Name: python3-module-%modulename
Version: 1.2
Release: alt1
Url: https://github.com/libfuse/pyfuse3/
Source: %origname-%version.tar
License: LGPL
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>

Patch: %origname-%version-alt.patch

BuildPreReq: libfuse3-devel >= 3.2.0
BuildRequires: python3-devel python3-module-Cython

Provides: %origname = %version-%release

%description
This is a Python interface to FUSE3.

FUSE (Filesystem in USErspace) is a simple interface for userspace
programs to export a virtual filesystem to the linux kernel. FUSE3
also aims to provide a secure method for non privileged users to
create and mount their own filesystem implementations.

%prep
%setup -n %origname-%version
%patch -p1

%build
%__python3 setup.py build_cython
%python3_build_debug

%install
%python3_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc LICENSE Changes.* README.* examples

%changelog
* Mon Jan 14 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.2-alt1
- Initial build for ALT Linux.
