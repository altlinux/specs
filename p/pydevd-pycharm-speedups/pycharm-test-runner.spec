%define _unpackaged_files_terminate_build 1

%define helperroot %_datadir/pycharm/helpers
%define nativeroot %_libdir/pycharm/helpers/pydev

Name: pydevd-pycharm-speedups
Version: 2026.2.4
Release: alt1

Summary: Native speedups and matching private Python helpers for PyCharm
License: Apache-2.0 and EPL-1.0 and MIT and BSD-3-Clause
Group: Development/Python3
Url: https://www.jetbrains.com/pycharm/
VCS: https://github.com/JetBrains/intellij-community.git

Source0: %name-%version.tar
Source1: %name-%version-pydev.tar
Source2: %name-%version-thriftpy.tar
Source3: %name-tests.tar
# Original license inputs outside the selected helper archives.
Source4: %name-licenses.tar
Patch0: %name-%version-alt-runner.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-java
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-Cython
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-coverage
BuildRequires: java-21-openjdk-devel
BuildRequires: gcc
BuildRequires: binutils

Requires: python3 >= 3.14
Requires: python3 < 3.15
Requires: pycharm-debugger = %version-%release

# The IDE explicitly selects these private import roots.
%add_findreq_skiplist %helperroot/*
%add_findprov_skiplist %helperroot/*

%description
Private unittest, pytest and doctest entry points with TeamCity protocol support.
The same source package builds the matching console schema, debugger runtime
and CPython speedups from the stable PyCharm helper sources.

%package -n pycharm-console-protocol
Summary: Private console protocol and transport helpers for PyCharm
Group: Development/Python3
BuildArch: noarch
Requires: python3 >= 3.14
Requires: python3 < 3.15

%description -n pycharm-console-protocol
Pinned console schema with the IDE's shaded ThriftPy2 and PLY transport.

%package -n pycharm-debugger
Summary: Matching private Python debugger runtime for PyCharm
Group: Development/Python3
BuildArch: noarch
Requires: python3 >= 3.14
Requires: python3 < 3.15
Requires: pycharm-console-protocol = %version-%release

%description -n pycharm-debugger
The stable PyCharm Python debugger runtime, including its actual private
modules, tracing, breakpoints, variable handling and console evaluator.

%package -n pycharm-test-runner
Summary: Private unittest, pytest and doctest runners for PyCharm
Group: Development/Python3
BuildArch: noarch
Requires: python3 >= 3.14
Requires: python3 < 3.15
Requires: python3-module-pytest

%description -n pycharm-test-runner
Pinned private test runners and TeamCity service-message support.

%prep
%setup
%patch0 -p1
tar xf %SOURCE1
mv %name-%version-pydev pydev
tar xf %SOURCE2
mv %name-%version-thriftpy thriftpy
tar xf %SOURCE3
mv %name-tests checks
cp checks/RunnerPeer.java .
tar xf %SOURCE4
mv %name-licenses licenses
cp pydev/LICENSE licenses/PyDev-LICENSE
if test -f thriftpy/LICENSE; then
    cp thriftpy/LICENSE licenses/ThriftPy-LICENSE
fi
# Existing binaries are never build inputs or installed payload.
find pydev -type f     \( -name '*.so' -o -name '*.pyd' -o -name '*.dll'     -o -name '*.exe' -o -name '*.jar' -o -name '*.class' \) -delete

%build
python3 -c 'import sys; assert sys.version_info[:2] == (3, 14)'
# Regenerate the stale PEP 669 C output with the unchanged upstream pyx.
(cd pydev && CFLAGS="%optflags" python3 setup_cython.py     --force-cython build_ext --inplace)

%install
while IFS= read -r path; do
    install -Dm644 "${path#pycharm/}" "%buildroot%helperroot/$path"
done < checks/PAYLOAD
python3 - %buildroot%helperroot %buildroot%nativeroot <<'PY'
from pathlib import Path
import shutil,sys
root,native=map(Path,sys.argv[1:])
skip={'build','build_tools','tests','stubs','ci-requirements','test-requirements',
      'pydev_tests','pydev_tests_mainloop','pydev_tests_python',
      'pydev_tests_runfiles','pydev_tests_tables','pydev_test_pydevd_reload'}
for path in Path('pydev').rglob('*'):
    relative=path.relative_to('pydev')
    if not path.is_file() or relative.parts[0] in skip:
        continue
    if path.name.lower().startswith('readme') or path.name in {
            'setup.py','setup_cython.py','conftest.py','pytest.ini','tox.ini'}:
        continue
    if path.suffix not in {'.py','.json','.thrift','.html','.js','.so'}:
        continue
    dest=root/'pydev'/relative
    dest.parent.mkdir(parents=True,exist_ok=True)
    if path.suffix=='.so':
        target=native/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,target)
        # The source package keeps Python data in datadir and ELF in libdir.
        dest.symlink_to(str(target).removeprefix('%buildroot'))
    else:
        shutil.copy2(path,dest)
for package in ('_shaded_thriftpy','_shaded_ply'):
    for path in (Path('thriftpy')/package).rglob('*.py'):
        relative=path.relative_to('thriftpy')
        if 'contrib' in relative.parts or path.name=='tornado.py':
            continue
        dest=root/'third_party/thriftpy'/relative
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,dest)
PY
# List the pure debugger payload separately from console and native modules.
find %buildroot%helperroot/pydev -type f \
    ! -path '*/pydev_console/*' | sed 's|^%buildroot||' > debugger.files
# The console owns pydev itself and its console subtree.
find %buildroot%helperroot/pydev -mindepth 1 -type d \
    ! -path '*/pydev_console' ! -path '*/pydev_console/*' \
    | sed 's|^%buildroot|%%dir |' >> debugger.files
find %buildroot%helperroot/pydev -type l \
    | sed 's|^%buildroot||' > speedups.files
find %buildroot%nativeroot -type f \
    | sed 's|^%buildroot||' >> speedups.files
find %buildroot%nativeroot -type d \
    | sed 's|^%buildroot|%%dir |' >> speedups.files

%check
python3 -I -B checks/check-protocol.py %buildroot%helperroot
python3 -I -B checks/check-debugger.py %buildroot%helperroot %buildroot%nativeroot
# Check runner outcomes and subtest node identities in both tree modes.
python3 -I -B checks/check-runners.py %buildroot%helperroot
# Exercise real coverage providers with the explicit summary option.
python3 -I -B checks/check-coverage.py %buildroot%helperroot coverage-results
# Match both pinned IDE summary settings and require exactly one counter set.
python3 -I -B checks/check-default-coverage.py %buildroot%helperroot default-coverage-results

# Exercise two real local workers, node outcomes and coverage counters.
python3 -I -B checks/check-xdist.py %buildroot%helperroot xdist-results

# Check real Unix socket delivery, stdout controls and transport precedence.
python3 -I -B checks/check-socket.py %buildroot%helperroot socket-results

# Check TCP delivery, default host and pre-execution connection failures.
python3 -I -B checks/check-tcp.py %buildroot%helperroot tcp-results

# Check repeated/nested unittest subtests with mixed outcomes in both trees.
python3 -I -B checks/check-nested.py %buildroot%helperroot nested-results

# Check expected outcomes and intact dotted subtest labels in both trees.
python3 -I -B checks/check-outcomes.py %buildroot%helperroot outcome-results

# Check fixture failures and subtest labels with method descriptions.
python3 -I -B checks/check-fixtures.py %buildroot%helperroot fixture-results

# Exercise a real JVM socket/process peer, workers, coverage and subtest output.
mkdir jvm-peer-classes
%_jvmdir/java-21-openjdk/bin/javac --release 11 -d jvm-peer-classes RunnerPeer.java
python3 -I -B checks/check-jvm-socket.py %buildroot%helperroot jvm-peer-classes \
    jvm-socket-results %_jvmdir/java-21-openjdk/bin/java

# Preserve parameter names, metadata and outcome nodes with real xdist workers.
python3 -I -B checks/check-params.py %buildroot%helperroot param-results

# Keep assertion diagnostics local to each fixture phase.
python3 -I -B checks/check-fixture-diagnostics.py %buildroot%helperroot fixture-diagnostic-results

# Preserve comparison fields and option parsing in two actual xdist workers.
python3 -I -B checks/check-xdist-diagnostics.py %buildroot%helperroot xdist-diagnostic-results

# Close failed test nodes after an actual worker crash and replacement.
python3 -I -B checks/check-worker-restart.py %buildroot%helperroot worker-restart-results

# Discover namespace directory paths with actual relative imports.
python3 -I -B checks/check-namespace.py %buildroot%helperroot namespace-results

# Check the pinned doctest CLI and Python3.14 statistics contract.
python3 -I -B checks/check-doctest.py %buildroot%helperroot doctest-results

# Exercise actual JVM process/stdout decoding of doctest service messages.
python3 -I -B checks/check-doctest-jvm.py %buildroot%helperroot jvm-peer-classes \
    doctest-jvm-results %_jvmdir/java-21-openjdk/bin/java

%files -n pycharm-test-runner
%dir %_datadir/pycharm
%dir %helperroot
%helperroot/pycharm

%files -n pycharm-console-protocol
%dir %helperroot/pydev
%helperroot/pydev/pydev_console
%helperroot/third_party

%files -n pycharm-debugger -f debugger.files

%files -f speedups.files
%doc licenses
%dir %_libdir/pycharm
%dir %_libdir/pycharm/helpers

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 2026.2.4-alt1
- Initial build for ALT.
