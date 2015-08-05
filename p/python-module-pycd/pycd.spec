%define oname pycd

%def_with python3

Name: python-module-%oname
Version: 0.3.17
Release: alt1.git20150803
Summary: Tool to change directory for python modules
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pycd
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wkentaro/pycd.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-clint
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-clint
%endif

%py_provides %oname
%py_requires clint

%description
Simple command line tool to change directory for python modules. You can
now easily read the codes of the modules.

%package -n %oname
Summary: Tool to change directory for python modules
Group: Development/Python
Requires: %name = %EVR

%description -n %oname
Simple command line tool to change directory for python modules. You can
now easily read the codes of the modules.

%package -n zsh-completion-%oname
Summary: Zsh completion for %oname
Group: Shells
Requires: %oname = %EVR

%description -n zsh-completion-%oname
Zsh completion for %oname.

%package -n bash-completion-%oname
Summary: Bash completion for %oname
Group: Shells
Requires: %oname = %EVR

%description -n bash-completion-%oname
Bash completion for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Tool to change directory for python modules
Group: Development/Python3
%py3_provides %oname
%py3_requires clint

%description -n python3-module-%oname
Simple command line tool to change directory for python modules. You can
now easily read the codes of the modules.

%package -n %{oname}3
Summary: Tool to change directory for python modules
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n %{oname}3
Simple command line tool to change directory for python modules. You can
now easily read the codes of the modules.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
install -d %buildroot%_sysconfdir/profile.d

%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
sed -i 's|pypack|pypack.py3|g' %oname.sh
sed -i 's|pycd|pycd3|g' %oname.sh
mv %oname.sh %buildroot%_sysconfdir/profile.d/%{oname}3.sh
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
mv %buildroot%_bindir/%oname.sh %buildroot%_sysconfdir/profile.d/

mv %buildroot%prefix%_sysconfdir/bash_completion.d \
	%buildroot%_sysconfdir/

%check
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
export PATH=$PATH:%buildroot%_bindir
source %buildroot%_sysconfdir/profile.d/%oname.sh
pycd clint
if [ "$PWD" != "%python_sitelibdir/clint" ]; then
	exit 1
fi
cd -
%if_with python3
pushd ../python3
python3 setup.py test
popd
source %buildroot%_sysconfdir/profile.d/%{oname}3.sh
pycd3 clint
if [ "$PWD" != "%python3_sitelibdir/clint" ]; then
	exit 1
fi
cd -
%endif

%files
%doc *.rst
%python_sitelibdir/*

%files -n %oname
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%_sysconfdir/profile.d/*

%files -n zsh-completion-%oname
%_datadir/zsh/site-functions/*

%files -n bash-completion-%oname
%_sysconfdir/bash_completion.d/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*

%files -n %{oname}3
%_bindir/*.py3
%_sysconfdir/profile.d/*
%endif

%changelog
* Wed Aug 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.17-alt1.git20150803
- Initial build for Sisyphus

