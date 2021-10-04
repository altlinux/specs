%define _unpackaged_files_terminate_build 1
%define oname isort

%def_with check

Name: python3-module-%oname
Version: 4.3.21
Release: alt2
Summary: Python utility / library to sort Python imports
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/isort
BuildArch: noarch

Source: %oname-%version.tar
Patch0: isort-4.3.21-Skip-tests-which-employ-extra-packages.patch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%add_python3_req_skip pylama.lint

%description
Python utility / library to sort Python imports

%prep
%setup -n %oname-%version
%autopatch -p2

%build
%python3_build

%install
%python3_install
mv %buildroot%_bindir/isort{,.py3}

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest test_isort.py {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v -- -v

%files
%doc README.rst LICENSE
%_bindir/isort.py3
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Tue Oct 05 2021 Ivan A. Melnikov <iv@altlinux.org> 4.3.21-alt2
- Get rid of pylama dependency.

* Thu Oct 17 2019 Stanislav Levin <slev@altlinux.org> 4.3.21-alt1
- 4.2.15 -> 4.3.21.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt2.qa1
- NMU: remove %%ubt from release

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt1.qa1
- NMU: applied repocop patch

* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.15-alt1
- Initial build for ALT.
