%define _unpackaged_files_terminate_build 1
%define oname argcomplete

%def_with check

Name: python-module-%oname
Version: 1.9.4
Release: alt2
Summary: Bash tab completion for argparse
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/argcomplete/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kislyuk/argcomplete.git
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-sphinx

%if_with check
BuildRequires: python-module-pexpect
BuildRequires: python3-module-pexpect
BuildRequires: python3-module-tox
BuildRequires: /dev/pts
BuildRequires: tcsh
%endif

%description
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

* You're using bash or zsh as your shell
* You're using argparse to manage your command line arguments/options

%package -n python3-module-%oname
Summary: Bash tab completion for argparse
Group: Development/Python3

%description -n python3-module-%oname
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

* You're using bash or zsh as your shell
* You're using argparse to manage your command line arguments/options

%prep
%setup -n %oname-%version

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

export PYTHONPATH=$PWD
%make -C docs html
mkdir man
cp -fR docs/*/html/* man/

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

%check
export LC_ALL=C.UTF-8
export TOX_TESTENV_PASSENV='LC_ALL'
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst man/ docs/examples
%_bindir/activate-global-python-argcomplete
%_bindir/python-argcomplete-check-easy-install-script
%_bindir/python-argcomplete-tcsh
%_bindir/register-python-argcomplete
%python_sitelibdir/argcomplete/
%python_sitelibdir/argcomplete-*.egg-info/

%files -n python3-module-%oname
%doc *.rst man/ docs/examples
%_bindir/activate-global-python-argcomplete.py3
%_bindir/python-argcomplete-check-easy-install-script.py3
%_bindir/python-argcomplete-tcsh.py3
%_bindir/register-python-argcomplete.py3
%python3_sitelibdir/argcomplete/
%python3_sitelibdir/argcomplete-*.egg-info/

%changelog
* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 1.9.4-alt2
- Dropped BR on python argparse.
- Enabled testing.

* Wed Mar 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9.4-alt1
- Updated version to 1.9.4

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1.git20141109.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20141109.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1.git20141109.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20141109
- Version 0.8.3

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141103
- Version 0.8.2
- Enabled testing

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20141005
- Initial build for Sisyphus
