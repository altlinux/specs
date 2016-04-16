%define oname ytfs

Name: %oname
Version: 0.99
Release: alt1.20160217.1

Summary: File system which enables you to search and play movies from YouTube as files 
License: MIT
Group: Networking/File transfer

Url: https://pypi.python.org/pypi/%oname/
#Url: https://github.com/rasguanabana/ytfs.git
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3 
BuildPreReq: python3-module-setuptools
Requires: python3-module-%oname = %version
Requires: python3-module-requests

%description
File system which enables you to search and play movies from YouTube as files -
with tools of your choice. Based on FUSE, written in Python 3.

%package -n python3-module-%oname
Summary: %oname bindings for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
File system which enables you to search and play movies from YouTube as files -
with tools of your choice. Based on FUSE, written in Python 3.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%oname

%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Sat Apr 16 2016 Anton Midyukov <antohami@altlinux.org> 0.99-alt1.20160217.1
- Initial build for Alt Linux Sisyphus.
