%global oname testpath

%def_with python3

Name:           python-module-%oname
Version:        0.3.1
Release:        alt1
Summary:        Test utilities for code working with files and commands
BuildArch:      noarch
License:        MIT
Group:          Development/Python
URL:            https://github.com/jupyter/testpath

# https://github.com/jupyter/testpath.git
Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python2.7(sphinx) python2.7(sphinx_rtd_theme)
BuildRequires: python2.7(pytest) python2.7(pathlib2)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(pytest) python3(pathlib2)
%endif

%description
Testpath is a collection of utilities for Python code working with files and
commands.

It contains functions to check things on the filesystem, and tools for
mocking system commands and recording calls to those.

%package        doc
Summary:        %{name} documentation
Group: Development/Documentation

%description doc
Documentation for %{name}.

%if_with python3
%package -n python3-module-%oname
Summary: Test utilities for code working with files and commands
Group: Development/Python3

%description -n python3-module-%oname
Testpath is a collection of utilities for Python code working with files and
commands.

It contains functions to check things on the filesystem, and tools for
mocking system commands and recording calls to those.
%endif

%prep
%setup

# The exe files are not needed
rm -f %oname/*.exe

%if_with python3
cp -fR . ../python3
%endif

%build
# generate html docs
make -C doc html

%install
install -d %buildroot%python_sitelibdir
cp -ar testpath %buildroot%python_sitelibdir/testpath

%if_with python3
pushd ../python3
install -d %buildroot%python3_sitelibdir
cp -ar testpath %buildroot%python3_sitelibdir/testpath
popd
%endif

%check
python -m pytest -v

%if_with python3
pushd ../python3
python3 -m pytest -v
popd
%endif

%files
%doc README.rst LICENSE
%python_sitelibdir/%oname

%files doc
%doc doc/_build/html

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%endif

%changelog
* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.1-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-1
- New version 0.3.1 (#1455375)
- Uses pathlib2 instead of pathlib

* Wed Mar 08 2017 Miro Hrončok <mhroncok@redhat.com> - 0.3-1
- initial package

