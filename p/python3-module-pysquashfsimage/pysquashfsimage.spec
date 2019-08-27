%define oname pysquashfsimage

Name:        python3-module-%oname
Version:     0.6
Release:     alt2.git.e06808f

Summary:     Python library to read Squashfs image files. 
License:     %gpl3only/%lgpl21only
Group:       Development/Python3
Url:         https://github.com/matteomattei/PySquashfsImage
BuildArch:   noarch

Source:      %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-licenses
BuildPreReq:        python3-module-setuptools python3-devel


%description
PySquashfsImage is a lightweight library for reading squashfs image files in 
Python. It provides a way to read squashfs images header and to retrieve 
encapsulated binaries. It is compatible with Python2 and Python3.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.GPL3 LICENSE.LGPL README.md
%python3_sitelibdir/*

%changelog
* Tue Aug 27 2019 Ivan Razzhivin <underwit@altlinux.org> 0.6-alt2.git.e06808f
- build from git

* Thu Jul 11 2019 Ivan Razzhivin <underwit@altlinux.org> 0.6-alt1
- Initial build for ALT Linux Sisyphus
