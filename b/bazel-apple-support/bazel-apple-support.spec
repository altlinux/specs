%define _unpackaged_files_terminate_build 1

Name: bazel-apple-support
Version: 2.11.0
Release: alt1

Summary: Offline source provider for Bazel apple_support
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/bazelbuild/apple_support
VCS: https://github.com/bazelbuild/apple_support.git

Source0: %name-%version.tar
Source1: apple_support.%version-release.tar.gz
Source2: registry.tar.gz
Source3: UPSTREAM.txt
BuildArch: noarch
AutoReqProv: no

BuildRequires: python3
BuildRequires: patch

%description
Provides the complete apple_support %version upstream source tree and a local
Bzlmod registry entry for offline Bazel consumers.

%prep
%setup -q
mkdir -p %_builddir/release-source %_builddir/registry-verify
tar -xzf %SOURCE1 -C %_builddir/release-source
tar -xzf %SOURCE2 -C %_builddir/registry-verify

%build

%check
test "$(sha256sum %SOURCE1 | cut -d' ' -f1)" = \
    447506cead9e3a2c382b4780f4fab8dbb8f6c3f7df309a7914247262c5f51e00
grep -F 'name = "apple_support"' MODULE.bazel
python3 - %SOURCE1 %_builddir/registry-verify/registry <<'PYREGISTRY'
from pathlib import Path
import base64,hashlib,json,sys
archive,registry=map(Path,sys.argv[1:])
module=registry/'modules/apple_support/%version'
source=json.loads((module/'source.json').read_text())
assert source['url']=='file://%_datadir/bazel/apple_support/distdir/apple_support.%version.tar.gz'
assert base64.b64decode(source['integrity'].split('-',1)[1])==hashlib.sha256(archive.read_bytes()).digest()
assert 'version = "%version"' in (module/'MODULE.bazel').read_text()
assert json.loads((registry/'modules/apple_support/metadata.json').read_text())['versions']==['%version']
for name,integrity in source['patches'].items():
    assert base64.b64decode(integrity.split('-',1)[1])==hashlib.sha256((module/'patches'/name).read_bytes()).digest()
print('Official archive and BCR patch integrity, genuine single-version local registry PASS')
PYREGISTRY
patch --batch -p1 -d %_builddir/release-source \
    -i %_builddir/registry-verify/registry/modules/apple_support/%version/patches/module_dot_bazel_version.patch
grep -F 'version = "%version"' %_builddir/release-source/MODULE.bazel

%install
install -d %buildroot%_datadir/bazel/apple_support/%version
cp -a . %buildroot%_datadir/bazel/apple_support/%version/
# Preserve README in authentic archives, outside the installed source view.
find %buildroot%_datadir/bazel/apple_support/%version \
    '(' -type f -o -type l ')' -iname 'readme*' -delete
install -d %buildroot%_datadir/bazel/apple_support/distdir
install -pm644 %SOURCE1 \
    %buildroot%_datadir/bazel/apple_support/distdir/apple_support.%version.tar.gz
tar -xzf %SOURCE2 -C %buildroot%_datadir/bazel/apple_support
cp -p %SOURCE3 .

%files
%doc LICENSE UPSTREAM.txt
%_datadir/bazel/apple_support

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 2.11.0-alt1
- Initial build for ALT.
