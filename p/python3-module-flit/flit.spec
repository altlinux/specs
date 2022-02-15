%define _unpackaged_files_terminate_build 1

%define oname flit

%def_disable bootstrap

Name: python3-module-%oname
Version: 3.6.0
Release: alt1
Summary: Simplified packaging of Python modules
# ./flit/logo.py  under ASL 2.0 license
# ./flit/upload.py under PSF license
License: BSD-3-Clause and Apache-2.0 and Python
Group: Development/Python3
URL: https://flit.readthedocs.io/en/latest/

BuildArch: noarch

# https://github.com/takluyver/flit
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pip python3-module-requests python3-module-docutils
BuildRequires: python3(pygments)
BuildRequires: python3(toml)

%if_enabled bootstrap
%add_python3_req_skip requests_download
%endif

%py3_requires pip
%py3_requires pygments

%description
Flit is a simple way to put Python packages and modules on PyPI.

Flit only creates packages in the new 'wheel' format. People using older
versions of pip (<1.5) or easy_install will not be able to install them.

Flit packages a single importable module or package at a time, using the import
name as the name on PyPI. All subpackages and data files within a package are
included automatically.

Flit requires Python 3, but you can use it to distribute modules for Python 2,
so long as they can be imported on Python 3.

%prep
%setup

%build
export PYTHONPATH=$(pwd)/flit_core
export FLIT_NO_NETWORK=1

pushd flit_core &>/dev/null
python3 -c 'from flit_core.buildapi import build_wheel; build_wheel(".")'
mkdir ../dist
mv flit_core-%version-*-none-any.whl ../dist
popd &>/dev/null

python3 -m flit build --format wheel

%install
pip3 install -I dist/flit_core-%version-*-none-any.whl --root %buildroot --prefix %prefix --no-deps
pip3 install -I dist/%oname-%version-*-none-any.whl --root %buildroot --prefix %prefix --no-deps

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/flit
%python3_sitelibdir/flit-%version.dist-info
%python3_sitelibdir/flit_core
%python3_sitelibdir/flit_core-%version.dist-info
%_bindir/flit

%changelog
* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.0-alt1
- Updated to upstream version 3.6.0.

* Tue Aug 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0.

* Tue Jun 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt1
- Updated to upstream version 3.2.0.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1
- Updated to upstream version 3.0.0.

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt2
- Disabled bootstrapping.

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Michal Cyprian <mcyprian@redhat.com> - 0.9-5
- Use python install wheel macro

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-4
- Rebuild for Python 3.6

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9-3
- Updated spec file with license comments and provides

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9-2
- spec file cleanup

* Sat Jul 2 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.9-1
- Initial RPM release
