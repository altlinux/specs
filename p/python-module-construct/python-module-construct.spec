%def_with python3

Summary: A powerful declarative parser/builder for binary data
Name: python-module-construct
Version: 2.5.1
Release: alt1
License: MIT
Group: Development/Python
Url: http://construct.readthedocs.org
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python python-devel
%if_with python3
BuildRequires: rpm-build-python3 python3-devel
%endif

Requires: python-module-six

%description
Construct is a powerful declarative parser (and builder) for binary
data.

Instead of writing imperative code to parse a piece of data, you
declaratively define a data structure that describes your data. As
this data structure is not code, you can use it in one direction to
parse data into Pythonic objects, and in the other direction, convert
(build) objects into binary data.

%if_with python3
%package -n     python3-module-construct
Summary: A powerful declarative parser/builder for binary data
Group: Development/Python
Requires: python3-module-six

%description -n python3-module-construct
Construct is a powerful declarative parser (and builder) for binary
data.

Instead of writing imperative code to parse a piece of data, you
declaratively define a data structure that describes your data. As
this data structure is not code, you can use it in one direction to
parse data into Pythonic objects, and in the other direction, convert
(build) objects into binary data.

This is the Python 3 version of the package.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst LICENSE
%python_sitelibdir/construct
%python_sitelibdir/construct-%version-py?.?.egg-info

%if_with python3
%files -n python3-module-construct
%doc README.rst LICENSE
%python3_sitelibdir/construct
%python3_sitelibdir/construct-%version-py?.?.egg-info
%endif

%changelog
* Mon Dec 12 2016 Lenar Shakirov <snejok@altlinux.ru> 2.5.1-alt1
- Initial build for ALT (based on 2.5.1-8.fc25.src)

