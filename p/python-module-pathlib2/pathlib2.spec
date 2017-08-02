%global oname	pathlib2
%def_with python3

Name:           python-module-%oname
Version:        2.1.0
Release:        alt1
Summary:        Object-oriented filesystem paths
License:        MIT
Group: Development/Python
URL:            https://github.com/mcmtroffaes/pathlib2
Source0:        %name-%version.tar.gz
BuildArch:      noarch

%global _description \
The old pathlib module on bitbucket is in bugfix-only mode. The goal of\
pathlib2 is to provide a backport of standard pathlib module which tracks\
the standard library module, so all the newest features of the standard\
pathlib can be used also on older Python versions.

%description %{_description}

BuildRequires(pre): python-modules
BuildRequires(pre): python-test
BuildRequires(pre): python-module-six
BuildRequires(pre): python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): python3(io)
BuildRequires(pre): python3-test
BuildRequires(pre): python3-module-six
BuildRequires(pre): python3-module-setuptools
%endif

%package -n python3-module-%oname
Group: Development/Python
Summary:        %{summary}

%description -n python3-module-%oname %{_description}

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

%check
for test in test_pathlib2.py test_pathlib2_with_py2_unicode_literals.py; do
    python $test
done

%if_with python3
pushd ../python3
for test in test_pathlib2.py test_pathlib2_with_py2_unicode_literals.py; do
    python3 $test
done
%endif
popd

%files
%doc README.rst
%doc LICENSE.rst
%python_sitelibdir/%oname.py*
%python_sitelibdir/%oname-%version-py?.?.egg-info

%files -n python3-module-%oname
%doc README.rst
%doc LICENSE.rst
%python3_sitelibdir/%oname.py*
%python3_sitelibdir/%oname-%version-py?.?.egg-info
%python3_sitelibdir/__pycache__/*

%changelog
* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-2
- Add %%check.
- Change URL from pathlib to pathlib2 page.

* Mon Nov 14 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-1
- Initial package.
