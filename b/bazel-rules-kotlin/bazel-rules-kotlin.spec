%define _unpackaged_files_terminate_build 1
# Preserve actual source data, including upstream .gitignore and templates.
%set_cleanup_method skip

Name: bazel-rules-kotlin
Version: 2.4.21
Release: alt2

Summary: Kotlin rules sources for Bazel
License: Apache-2.0
Group: Development/Other
Url: https://github.com/bazel-contrib/rules_kotlin
VCS: https://github.com/bazel-contrib/rules_kotlin.git
BuildArch: noarch
# Bazel is available on these build architectures.
ExclusiveArch: x86_64 aarch64
# Embedded source scripts are build inputs, not installed application tools.
AutoReqProv: no

Source0: %name-%version.tar
Patch0: %name-alt.patch
Source1: source-provenance.alt
Source2: upstream-files.sha256

Source3: rules-kotlin-worker-build.tar
Source4: worker-registry.tar.gz
Source5: bazel-worker-api-v0.0.11.tar.gz
Patch2: rules-jvm-external-unpinned.patch
Patch1: 0001-Bootstrap-workers-with-system-tools.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: python3
BuildRequires: bazel
BuildRequires: bazel-java-builder
BuildRequires: bazel-java-tools-native
BuildRequires: bazel-rules-jvm-external
BuildRequires: bazel-toml
BuildRequires: java-21-openjdk-devel
BuildRequires: gcc-c++
BuildRequires: protobuf-bazel
BuildRequires: mvn(codes.rafael.asmjdkbridge:asm-jdk-bridge)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-aa)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-api)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-common-deps)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.j2objc:j2objc-annotations)
BuildRequires: mvn(org.altlinux.bootstrap:bazel-java-tools-coverage)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.jacoco:org.jacoco.agent::runtime:)
BuildRequires: mvn(org.jacoco:org.jacoco.core)
BuildRequires: mvn(org.jacoco:org.jacoco.report)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlin:jvm-abi-gen)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-annotation-processing)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-build-tools-api)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-compiler)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-script-runtime)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.ow2.asm:asm-tree)
BuildRequires: mvn(org.pantsbuild:jarjar)

%description
Complete genuine stable mainline rules_kotlin source tree, installed in
%_datadir/bazel/rules/rules_kotlin for local Bazel repository integration.
Includes compiler worker sources, Starlark rules, tests and examples.

%package workers
Summary: Kotlin compiler workers for Bazel
License: Apache-2.0 AND BSD-3-Clause AND EPL-2.0
Group: Development/Other

%description workers
Release module with Kotlin compiler workers, dependency metadata tools
and symbol processing support built from the rules_kotlin sources.

%prep
%setup -q -c -T -n %name-%version-workers
%setup
sha256sum -c %SOURCE2
%patch0 -p1
sed -i 's/^    version = "2\.2\.0",$/    version = "%version",/' MODULE.bazel

cp -a . ../%name-%version-workers/
pushd ../%name-%version-workers
tar -xf %SOURCE3 --strip-components=1
%patch1 -p1
cp -a %_datadir/bazel/rules/rules_jvm_external .rpm-sources/
patch -d .rpm-sources/rules_jvm_external -p1 -i %PATCH2
popd

%build
pushd ../%name-%version-workers
bash build-workers.sh %SOURCE4 %SOURCE5 %_jvmdir/java-21-openjdk \
    "${NPROCS:-%__nprocs}"
install -m 0644 bazel-bin/rules_kotlin_release.tgz %_builddir/%name-workers.tgz
popd

%install
install -d %buildroot%_datadir/bazel/rules/rules_kotlin
cp -a . %buildroot%_datadir/bazel/rules/rules_kotlin/
find %buildroot%_datadir/bazel/rules/rules_kotlin -type d -exec chmod 755 {} +
find %buildroot%_datadir/bazel/rules/rules_kotlin -type f \
    -exec chmod u+rw,go+r,go-w {} +
find %buildroot%_datadir/bazel/rules/rules_kotlin \
    '(' -type f -o -type l ')' -iname 'readme*' -delete
# Keep packaging documentation outside the installed source tree.
cp -p %SOURCE1 %SOURCE2 .

install -d %buildroot%_datadir/bazel/rules/rules_kotlin-workers
tar -xf %_builddir/%name-workers.tgz \
    -C %buildroot%_datadir/bazel/rules/rules_kotlin-workers
install -pm 0644 kotlin/compiler/compiler.bzl \
    %buildroot%_datadir/bazel/rules/rules_kotlin-workers/kotlin/compiler/

worker_docs=%buildroot%_docdir/%name-workers-%version
jacoco_docs=%_docdir/jacoco-$(rpm -q --qf '%%{VERSION}' jacoco)
asm_docs=%_docdir/objectweb-asm-$(rpm -q --qf '%%{VERSION}' objectweb-asm)
install -d "$worker_docs"
install -pm 0644 %_datadir/bazel/rules/protobuf/LICENSE \
    "$worker_docs/LICENSE-Protobuf"
install -pm 0644 "$jacoco_docs/LICENSE.md" "$worker_docs/LICENSE-JaCoCo.md"
install -pm 0644 "$asm_docs/LICENSE.txt" "$worker_docs/LICENSE-ASM.txt"

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

%files workers
%doc %_docdir/%name-workers-%version/
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_kotlin-workers/

%changelog
* Thu Nov 26 2026 Ivan Khanas <xeno@altlinux.org> 2.4.21-alt2
- Package the Kotlin workers built from source.

* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 2.4.21-alt1
- Initial build for ALT.
