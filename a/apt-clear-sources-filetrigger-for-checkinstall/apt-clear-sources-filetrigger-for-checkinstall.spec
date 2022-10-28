Name: apt-clear-sources-filetrigger-for-checkinstall
Version: 1
Release: alt1

Summary: Ensure that any APT's sources are deleted (a helper pkg for *-checkinstall pkgs)
Group: Development/Other
License: ALT-Public-Domain

# This dep simplifies how this package shall be used in order to avoid
# the problem with the files in question not having been deleted yet
# at the moment when this is needed, namely, at the moment of a transaction
# when a *-checkinstall package with a test for apt is installed.
#
# Normally, a *-checkinstall package with a test for apt would have a
# dep on apt and cause the installation of apt in the same transaction
# where its test scripts are run. But our "cleaning" filetrigger would
# then only have an effect at the end of the transaction: that's a
# problem, because the test wouldn't be run with clean APT's sources
# (although we'd want this).
Requires(post): apt
Requires: apt

BuildArch: noarch

Source1: apt-clear-sources-filetrigger-for-checkinstall.filetrigger

%description
%summary.

This package is not intended for installation in normal systems.
Its sole purpose is to help the automatic testing of apt in hasher
with package repositiories where the default build env contains
uncommented external sources for APT (inaccessible in hasher).

For this package to have an effect at the moment when a *-checkinstall
package with tests for APT is installed, apt (and friends with sources.list)
must be installed in a separate previous transaction. (Otherwise
the effect would only happen at the end of the current transaction,
rather than before the testing scripts are run.)

A simple way to achieve this is to install this packages in a separate
transaction (and this package has a dep on apt).

%install
install -m0755 -D %SOURCE1 %buildroot%_rpmlibdir/%name.filetrigger

%files
%_rpmlibdir/%name.filetrigger

%post
set -x
{
    echo 'Clearing the files that have been present before this pkg is installed.'
    rm -fv /etc/apt/sources.list{,.d/*} ||:
} >&2

%package checkinstall
Summary: Immediately install and check the effect of %name
Group: Development/Other

Requires: apt
Requires: %name

%description checkinstall
%summary.

%files checkinstall

%post checkinstall
set -efuC -o pipefail
set -x

find /etc/apt/sources.list.d/ -not -type d | { ! grep -Ee . >&2; }
! [ -e /etc/apt/sources.list ]

# Should not signal an error.
apt-get update

%changelog
* Fri Oct 28 2022 Ivan Zakharyaschev <imz@altlinux.org> 1-alt1
- Initial release (to help doing apt-BuildPreReq-under-pkdirect-checkinstall
  in repositories where the default build env contains external APT sources).
