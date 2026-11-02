%define _unpackaged_files_terminate_build 1
# Preserve actual source data, including upstream .gitignore and templates.
%set_cleanup_method skip

Name: bazel-rules-kotlin
Version: 2.4.21
Release: alt1

Summary: Kotlin rules sources for Bazel
License: Apache-2.0
Group: Development/Other
Url: https://github.com/bazel-contrib/rules_kotlin
VCS: https://github.com/bazel-contrib/rules_kotlin.git
BuildArch: noarch
# Embedded source scripts are build inputs, not installed application tools.
AutoReqProv: no

Source0: %name-%version.tar
Patch0: %name-alt.patch
Source1: source-provenance.alt
Source2: upstream-files.sha256

BuildRequires: python3

%description
Complete genuine stable mainline rules_kotlin source tree, installed in
%_datadir/bazel/rules/rules_kotlin for local Bazel repository integration.
Includes compiler worker sources, Starlark rules, tests and examples.

Bazel, JDK, Kotlin compiler and ordinary Bazel/Maven dependencies must be
provided separately. This source provider does not contain compiled workers.

%prep
%setup
# Verify the actual complete stable tag before the release metadata adaptation.
sha256sum -c %SOURCE2
%patch0 -p1
python3 - <<'PYVERSION'
from pathlib import Path
import re
p=Path('MODULE.bazel');text=p.read_text()
pattern=r'(module\(\s*name\s*=\s*"rules_kotlin",\s*version\s*=\s*)"2\.2\.0"'
text,count=re.subn(pattern,lambda m:m.group(1)+'"%version"',text,count=1)
assert count==1
p.write_text(text)
PYVERSION

%build
# The real compiler worker is built by its consuming Bazel toolchain.

%install
install -d %buildroot%_datadir/bazel/rules/rules_kotlin
cp -a . %buildroot%_datadir/bazel/rules/rules_kotlin/
find %buildroot%_datadir/bazel/rules/rules_kotlin -type d -exec chmod 755 {} +
find %buildroot%_datadir/bazel/rules/rules_kotlin -type f \
    -exec chmod u+rw,go+r,go-w {} +
find %buildroot%_datadir/bazel/rules/rules_kotlin \
    '(' -type f -o -type l ')' -iname 'readme*' -delete
# Relative %doc inputs are copied after the source view has been staged.
cp -p %SOURCE1 %SOURCE2 .

%check
python3 - %buildroot%_datadir/bazel/rules/rules_kotlin %SOURCE2 <<'PYCHECK'
from pathlib import Path
import hashlib,re,sys
root,manifest=map(Path,sys.argv[1:]);checked=0
for line in manifest.read_text().splitlines():
    digest,name=line.split('  ',1)
    if Path(name).name.lower().startswith('readme'):
        continue
    data=(root/name).read_bytes()
    assert data==Path(name).read_bytes(),name
    checked+=1
assert 'version = "%version"' in (root/'MODULE.bazel').read_text()
for name in ['kotlin/jvm.bzl','src/main/starlark/core/repositories/bzlmod_setup.bzl']:
    assert (root/name).stat().st_size>0
assert not any(p.name.lower().startswith('readme') for p in root.rglob('*'))
print('Genuine stable source file checks passed:',checked)
PYCHECK

%files
%doc LICENSE AUTHORS CONTRIBUTORS
%doc source-provenance.alt upstream-files.sha256
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_kotlin/

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 2.4.21-alt1
- Initial build for ALT.
