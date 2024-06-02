# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: shunit2
Version: 2.1.8
Release: alt1
Summary: shUnit2 is a xUnit based unit test framework for Bourne based shell scripts
License: Apache-2.0
Group: Development/Other
Url: https://github.com/kward/shunit2
BuildArch: noarch

Source: %name-%version.tar
%{?!_without_check:%{?!_disable_check:
BuildRequires: shellcheck
}}

%description
shUnit2 is a xUnit unit test framework for Bourne based shell scripts,
and it is designed to work in a similar manner to JUnit, PyUnit, etc.. If
you have ever had the desire to write a unit test for a shell script,
shUnit2 can do the job.

%prep
%setup
sed -i 's!\.\./shunit2!shunit2!' examples/*.sh

%install
install -Dp shunit2 -t %buildroot%_bindir

%check
# Self unit testing.
./test_runner
# Test actual run on examples.
PATH=%buildroot%_bindir:$PATH
cp -a examples /tmp/examples
pushd /tmp/examples
  ./equality_test.sh
! ./lineno_test.sh	|| exit 2
  ./math_test.sh
  ./mkdir_test.sh
  ./mock_file_test.sh
! ./output_test.sh	|| exit 2
! ./party_test.sh	|| exit 2
  ./suite_test.sh
rm -rf /tmp/examples
popd
# Upstream already tests for this.
shellcheck -e SC2086 shunit2

%files
%define _customdocdir %_docdir/%name
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%doc doc/* examples
%_bindir/shunit2

%changelog
* Sun Jun 02 2024 Vitaly Chikunov <vt@altlinux.org> 2.1.8-alt1
- First import v2.1.8-97-gda1e19d (2024-02-11).
