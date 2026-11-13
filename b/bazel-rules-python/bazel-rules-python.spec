%define _unpackaged_files_terminate_build 1

Name: bazel-rules-python
Version: 2.5.0
Release: alt1

Summary: Python rules and toolchain APIs for Bazel
License: Apache-2.0
Group: Development/Other
URL: https://github.com/bazel-contrib/rules_python
VCS: https://github.com/bazel-contrib/rules_python.git
BuildArch: noarch

Source0: %name-%version.tar
Source4: runfiles-pyproject.toml
Source6: %pyproject_deps_config_name
Patch0: module_dot_bazel_version.patch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3
BuildRequires: python3-module-pytest
BuildRequires: rpm-build-python3

# Bazel expands this polyglot template before it becomes an executable script.
%add_findreq_skiplist %_datadir/bazel/rules/rules_python/python/private/pypi/venv_entry_point_template.sh

%description
Bazel Starlark rules for Python binaries, libraries, tests, packaging, runfiles
and local interpreter toolchains. Provides the genuine rules_python module.

%package -n python3-module-bazel-runfiles
Summary: Python runfiles lookup library for Bazel programs
Group: Development/Python3
%pyproject_runtimedeps_metadata

%description -n python3-module-bazel-runfiles
Runfiles lookup and repository mapping from the complete rules_python source.
Provides the canonical runfiles wheel interface and the genuine python.runfiles
interface used by Bazel programs.

%prep
%setup
%autopatch -p1
mkdir -p .alt-runfiles/runfiles .alt-runfiles/python/runfiles
for package in .alt-runfiles/runfiles .alt-runfiles/python/runfiles; do
    cp -a python/runfiles/__init__.py python/runfiles/runfiles.py \
        python/runfiles/py.typed "$package/"
done
cp -a LICENSE .alt-runfiles/
cp %SOURCE4 .alt-runfiles/pyproject.toml
pushd .alt-runfiles
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
popd

%build
pushd .alt-runfiles
%pyproject_build
popd

%install
install -d %buildroot%_datadir/bazel/rules/rules_python
cp -a BUILD.bazel LICENSE MODULE.bazel WORKSPACE WORKSPACE.bzlmod \
    internal_dev_deps.bzl internal_dev_setup.bzl version.bzl \
    command_line_option crates python tools \
    %buildroot%_datadir/bazel/rules/rules_python/

pushd .alt-runfiles
%pyproject_install
popd


# The runfiles wheel target uses its README as a build input.
find %buildroot%_datadir/bazel -iname 'README*' \
    ! -path '*/python/runfiles/README.md' -delete

%check
# These two tests require Bazel-generated data and runfiles layout.
%__python3 -m pytest -q tests/runfiles/pathlib_test.py \
    tests/runfiles/runfiles_test.py \
    -k 'not testRlocationWithData and not testCurrentRepository' \
    --junitxml=runfiles-tests.xml

%files
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_python
%doc LICENSE

%files -n python3-module-bazel-runfiles
%python3_sitelibdir/runfiles
%dir %python3_sitelibdir/python
%python3_sitelibdir/python/runfiles
%python3_sitelibdir/%{pyproject_distinfo bazel_runfiles}

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 2.5.0-alt1
- Initial build for ALT.
