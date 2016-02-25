%define oname pytest-ansible
Name: python-module-%oname
Version: 1.2.4
Release: alt2.git20150318
Summary: Plugin for py.test to allow running ansible
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-ansible/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jlaska/pytest-ansible.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests ansible
BuildPreReq: python-module-pypandoc python-module-pycrypto
BuildPreReq: python-module-paramiko
BuildPreReq: python-modules-logging

%py_provides pytest_ansible
Requires: ansible
%py_requires logging

%description
This repository contains a plugin for py.test which adds several
fixtures for running ansible modules, or inspecting ansible_facts. While
one can simply call out to ansible using the subprocess module, having
to parse stdout to determine the outcome of the operation is unpleasant
and prone to error. With pytest-ansible, modules return JSON data which
you can inspect and act on, much like with an ansible playbook.

%prep
%setup

%build
%python_build_debug

%install
%python_install

for i in *.md; do
	rst=$(echo $i |sed 's|\.md||')
	python -c "import pypandoc; pypandoc.convert('$i', 'rst', format='markdown')" \
		>$rst.rst
done

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 1.2.4-alt2.git20150318
- Recompile.

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.git20150318
- Initial build for Sisyphus

