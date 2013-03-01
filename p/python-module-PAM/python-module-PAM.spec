Summary:	PAM bindings for Python
Name:		python-module-PAM
Version:	0.5.0
Release:	alt2
License:	LGPLv2
Group:		Development/Python
# Note that the upstream site is dead.
Source0:	%{name}-%{version}.tar.gz
Url:		http://www.pangalactic.org/PyPAM

Patch0:		%{name}-dlopen.patch
Patch1:		%{name}-0.5.0-dealloc.patch
Patch2:		%{name}-0.5.0-nofree.patch
Patch3:		%{name}-0.5.0-memory-errors.patch
Patch4:		%{name}-0.5.0-return-value.patch

BuildRequires:	python-devel
BuildRequires:	pam-devel
Requires:	python

Obsoletes:	python-module-pam

%description
PAM (Pluggable Authentication Module) bindings for Python.

%prep
%setup -q
%patch0 -p1 -b .dlopen
%patch1 -p1 -b .dealloc
%patch2 -p1 -b .nofree
%patch3 -p1 -b .memory
%patch4 -p1 -b .retval
# remove prebuild rpm and others binaries
rm -rf build dist

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %{__python} setup.py build

%install
%{__python} setup.py install --root=$RPM_BUILD_ROOT
# Make sure we don't include binary files in the docs
chmod 644 examples/pamtest.py
rm -f examples/pamexample

%files
%defattr(-, root, root, -)
%{python_sitelibdir}/PAMmodule.so
%{python_sitelibdir}/*.egg-info
%doc AUTHORS NEWS README ChangeLog COPYING INSTALL 
%doc examples

%changelog
* Fri Mar 01 2013 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt2
- Rename package to python-module-PAM

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt1
- Initial release for Sisyphus (based on Fedora)
