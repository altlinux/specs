%define _unpackaged_files_terminate_build 1
%define appdir %_datadir/%name

Name: cdxgen
Version: 12.8.4
Release: alt1

Summary: CycloneDX Software Bill of Materials generator
Group: Development/Tools
License: Apache-2.0
URL: https://cdxgen.github.io
VCS: https://github.com/cdxgen/cdxgen

BuildArch: noarch

Source0: %name-%version.tar

# npm install \
#      --omit=dev \
#      --include=optional \
#      --ignore-scripts
#
# node --input-type=module -e '
#  import { rmSync } from "node:fs";
#
#  for (const rubyPath of [
#    "node_modules/@appthreat/atom-parsetools/plugins/rubyastgen",
#    "node_modules/.bin/rubyastgen",
#  ]) {
#    rmSync(rubyPath, { recursive: true, force: true });
#  }
#  '
#
# cdxgen_native_files=$(find node_modules -type f \
#    \( -name '*.a' -o -name '*.dll' -o -name '*.dylib' \
#        -o -name '*.exe' -o -name '*.node' -o -name '*.so' \
#        -o -name '*.so.*' \) -print)
#
# test -z "$cdxgen_native_files" || {
#    echo "binary files found, need to clear"
#    echo "$cdxgen_native_files"
#    exit 1
# }
Source1: node_modules.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: node >= 20

Requires: node >= 20

AutoReq: no
AutoProv: no

%description
cdxgen creates CycloneDX Software Bill of Materials (SBOM) documents from
source trees, build manifests, container images and operating-system
installations. It supports multiple package ecosystems and can also produce
cryptography, operations, SaaS and AI BOM variants.

%prep
%setup -a1

%build

%install
install -d %buildroot%appdir
install -m0644 index.cjs package.json LICENSE README.md \
    %buildroot%appdir/
cp -a bin data lib types node_modules %buildroot%appdir/

install -d %buildroot%_bindir

for command in aibom cbom cdxgen cdxgen-secure obom saasbom spdxgen; do
    ln -sr %buildroot%appdir/bin/cdxgen.js \
        %buildroot%_bindir/$command
done

ln -sr %buildroot%appdir/bin/audit.js \
    %buildroot%_bindir/cdx-audit
ln -sr %buildroot%appdir/bin/convert.js \
    %buildroot%_bindir/cdx-convert
ln -sr %buildroot%appdir/bin/validate.js \
    %buildroot%_bindir/cdx-validate
ln -sr %buildroot%appdir/bin/verify.js \
    %buildroot%_bindir/cdx-verify
ln -sr %buildroot%appdir/bin/sign.js \
    %buildroot%_bindir/cdx-sign
ln -sr %buildroot%appdir/bin/repl.js \
    %buildroot%_bindir/cdxi
ln -sr %buildroot%appdir/bin/evinse.js \
    %buildroot%_bindir/evinse
ln -sr %buildroot%appdir/bin/hbom.js \
    %buildroot%_bindir/hbom

%files
%doc LICENSE README.md
%_bindir/aibom
%_bindir/cbom
%_bindir/cdx-audit
%_bindir/cdx-convert
%_bindir/cdx-sign
%_bindir/cdx-validate
%_bindir/cdx-verify
%_bindir/cdxgen
%_bindir/cdxgen-secure
%_bindir/cdxi
%_bindir/evinse
%_bindir/hbom
%_bindir/obom
%_bindir/saasbom
%_bindir/spdxgen
%appdir/

%changelog
* Tue Sep 01 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 12.8.4-alt1
- Update to version 12.8.4.

* Mon Aug 10 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 12.8.2-alt1
- Initial build.
