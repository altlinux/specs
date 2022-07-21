Name: python3-module-construct
Version: 2.10.68
Release: alt1

Summary: A powerful declarative parser/builder for binary data
License: MIT
Group: Development/Python
Url: https://pypi.org/project/construct/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(arrow)
BuildRequires: python3(cloudpickle)
BuildRequires: python3(lz4)
BuildRequires: python3(numpy)
BuildRequires: python3(ruamel)

%description
Construct is a powerful declarative parser (and builder) for binary
data.

Instead of writing imperative code to parse a piece of data, you
declaratively define a data structure that describes your data. As
this data structure is not code, you can use it in one direction to
parse data into Pythonic objects, and in the other direction, convert
(build) objects into binary data.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
py.test3 tests/ -k 'not benchmark' --showlocals --verbose

%files
%doc README.rst LICENSE
%python3_sitelibdir/construct
%python3_sitelibdir/construct-%version.dist-info

%changelog
* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.10.68-alt1
- 2.10.68 released

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.10.56-alt1
- 2.10.56 released

* Mon Dec 12 2016 Lenar Shakirov <snejok@altlinux.ru> 2.5.1-alt1
- Initial build for ALT (based on 2.5.1-8.fc25.src)
