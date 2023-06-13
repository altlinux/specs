%define  modulename umsgpack
%define  srcname u-msgpack-python

Name:    python3-module-%modulename
Version: 2.8.0
Release: alt1

Summary: A portable, lightweight MessagePack serializer and deserializer
License: MIT
Group:   Development/Python3
URL:     https://github.com/vsergeev/u-msgpack-python

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: pytest3

BuildArch: noarch

Source:  %srcname-%version.tar

%description
u-msgpack-python is a lightweight MessagePack serializer and deserializer
module written in pure Python, compatible with both Python 2 and 3, as
well CPython and PyPy implementations of Python. u-msgpack-python is fully
compliant with the latest MessagePack specification. In particular, it
supports the new binary, UTF-8 string, application-defined ext, and
timestamp types.

%prep
%setup -n %srcname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
pytest3 -v

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/u_msgpack_python-%version.dist-info

%changelog
* Tue Jun 13 2023 Anton Midyukov <antohami@altlinux.org> 2.8.0-alt1
- New version 2.8.0.

* Wed May 19 2021 Anton Midyukov <antohami@altlinux.org> 2.7.1-alt1
- new version 2.7.1

* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 2.5.1-alt1
- new version 2.5.1

* Tue Aug 21 2018 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
