Name: pyfda
Version: 0.9.5
Release: alt2

Summary: Python Filter Design Analysis Tool
License: MIT
Group: Development/Other
Url: https://github.com/chipmuenk/pyfda

Source0: %name-%version.tar
Patch0: 0001-Fix-numpy-import-for-NumPy-2.x-compatibility.patch

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
pyfda is a tool written in Python / Qt for analyzing and designing
discrete time filters with a user-friendly GUI. Fixpoint filter
implementations (for some filter types) can be simulated and tested
for overflow and quantization behaviour in the time and frequency domain.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# not yet
%add_python3_req_skip amaranth amaranth.back amaranth.sim
%add_python3_req_skip nmigen nmigen.back nmigen.sim
# odd self-contained relative imports
%add_python3_req_skip bak.delay.fixpoint_helpers
%add_python3_req_skip pyfda.fixpoint_widgets.fixpoint_helpers
%add_python3_req_skip pyfda.fixpoint_widgets.old.delay.fixpoint_helpers
%add_python3_req_skip pyfda.fixpoint_widgets.fixpoint_helpers_nmigen
%add_python3_req_skip pyfda.compat

%files
%_bindir/pyfdax
%python3_sitelibdir/bak
%python3_sitelibdir/pyfda
%python3_sitelibdir/pyfda-%version.dist-info

%changelog
* Tue Jun 3 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.9.5-alt2
- Compatible with NumPy 2.x

* Fri Apr 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.5-alt1
- 0.9.5 released

