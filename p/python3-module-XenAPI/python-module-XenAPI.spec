%define modulename XenAPI

Name: python3-module-%modulename
Summary: XenAPI SDK
Version: 1.127.1

Release: alt1
License: LGPL 2.1
Group: Development/Python3
URL: http://community.citrix.com/display/xs/Download+SDKs
BuildArch: noarch

Source: %name-%version.tar.gz
Patch0: fix-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
XenAPI SDK, for communication with Citrix XenServer and Xen Cloud Platform.
Geraldo is a Python and Django pluggable application
that works with ReportLab to generate complex reports.

%prep
%setup
%patch -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/*


%changelog
* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.127.1-alt1
- Version updated to 1.127.1
- porting on python3

* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.2-alt1
- Initial build for ALT
