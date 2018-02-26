%define oname BytecodeAssembler
Name: python-module-peak-util-%oname
Version: 0.6
Release: alt1.1

Summary: peak.util.assembler is a simple bytecode assembler module

License: PSF or ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/%oname/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: python-module-setuptools

Requires: python-module-peak

Requires: python-module-peak-util-SymbolType

%setup_python_module %oname

Source: http://pypi.python.org/packages/source/B/%oname/%oname-%version.tar

%description
peak.util.assembler is a simple bytecode assembler module that handles
most low-level bytecode generation details like jump offsets, stack size
tracking, line number table generation, constant and variable name index
tracking, etc. That way, you can focus your attention on the desired
semantics of your bytecode instead of on these mechanical issues.

In addition to a low-level opcode-oriented API for directly generating
specific Python bytecodes, this module also offers an extensible mini-AST
framework for generating code from high-level specifications. This
framework does most of the work needed to transform tree-like structures
into linear bytecode instructions, and includes the ability to do
compile-time constant folding.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/peak/util/*
%python_sitelibdir/%{oname}*.egg-info
%python_sitelibdir/%{oname}*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1.1
- Rebuild with Python-2.7

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- new version (0.6) import in git

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus

