# SPDX-License-Identifier: GPL-2.0-only
Name: egrep-callers
Summary: Wrapper egrep/fgrep to show callers
Version: 1
Release: alt1
License: GPL-2.0-only
Group: Development/Debug
Url: https://lists.altlinux.org/pipermail/devel/2022-May/216776.html

Source: %name-%version.tar
BuildArch: noarch
BuildRequires: shellcheck

# /proc is required to work in the hasher
Requires: /proc

%description
Help to find invocators of egrep/fgrep.

%package checkinstall
Summary: %summary
Group: %group
Requires(pre): %name = %EVR

%description checkinstall
Test %summary.

%prep
%setup

%build
bash -n egrep
bash -n filetrigger
shellcheck egrep filetrigger

%install
install -Dp egrep	%buildroot%_bindir/egrep.callers
install -Dp filetrigger	%buildroot%_rpmlibdir/egrep.filetrigger

%post
echo %_bindir/fgrep | %_rpmlibdir/egrep.filetrigger

%pre checkinstall
set -eux -o pipefail
fgrep root /etc/passwd | sed s/^/:/

%files
%_bindir/egrep.callers
%_rpmlibdir/egrep.filetrigger

%files checkinstall

%changelog
* Mon Jun 27 2022 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
