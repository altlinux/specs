%def_with python3

%global modname munch

Name:               python-module-munch
Version:            2.1.1
Release:            alt1
Summary:            A dot-accessible dictionary (a la JavaScript objects)

Group:              Development/Python
License:            MIT
URL:                https://pypi.io/project/munch
Source0:            %name-%version.tar

BuildArch:          noarch

BuildRequires:      python-devel
BuildRequires:      python-module-setuptools

%if_with python3
BuildRequires:      rpm-build-python3
BuildRequires:      python3-module-setuptools
%endif

%description
munch is a fork of David Schoonover's **Bunch** package, providing similar
functionality. 99 percent of the work was done by him, and the fork was made
mainly for lack of responsiveness for fixes and maintenance on the original
code.

Munch is a dictionary that supports attribute-style access, a la
JavaScript.

%if_with python3
%package -n python3-module-munch
Summary:            A dot-accessible dictionary (a la JavaScript objects)
Group:              Development/Python

%description -n python3-module-munch
munch is a fork of David Schoonover's **Bunch** package, providing similar
functionality. 99 percent of the work was done by him, and the fork was made
mainly for lack of responsiveness for fixes and maintenance on the original
code.

Munch is a dictionary that supports attribute-style access, a la
JavaScript.
%endif

%prep
%setup

# Remove shebang to make rpmlint happy.
sed -i '/\/usr\/bin\/python/d' munch/__init__.py

# Remove bundled egg-info in case it exists
rm -rf %modname.egg-info
%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc README.md LICENSE.txt
%python_sitelibdir/%modname/
%python_sitelibdir/%modname-%{version}*

%if_with python3
%files -n python3-module-munch
%doc README.md LICENSE.txt
%python3_sitelibdir/%modname/
%python3_sitelibdir/%modname-%{version}*
%endif

%changelog
* Tue Jun 13 2017 Lenar Shakirov <snejok@altlinux.ru> 2.1.1-alt1
- Initial build for ALT (based on 2.1.1-1.fc27.src)

