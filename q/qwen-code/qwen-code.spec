%global _unpackaged_files_terminate_build 1
# git rev-parse --short v%version
%global commit_hash ebc2a01

Name: qwen-code
Version: 0.10.6
Release: alt1
Summary: AI-powered command-line workflow tool for developers
License: Apache-2.0
Group: Development/Tools
Url: https://qwenlm.github.io/qwen-code-docs
VCS: https://github.com/QwenLM/qwen-code

Source: %name-%version.tar
Source1: node_modules.tar
Source2: node_modules_cli.tar
Source3: node_modules_core.tar
Source4: qwen.sh

BuildArch: noarch

BuildRequires: esbuild
BuildRequires: npm

%description
QwenCode is a powerful command-line AI workflow tool adapted
from Gemini CLI, specifically optimized for Qwen3-Coder models.
It enhances your development workflow with advanced code
understanding, automated tasks, and intelligent assistance.

%prep
# ./alt/update_modules.sh
%setup -a 1 -a 2 -a 3
mkdir -p packages/{core,cli}/src/generated
tee packages/{core,cli}/src/generated/git-commit.{js,ts} <<EOF
export const GIT_COMMIT_INFO = '%commit_hash';
export const CLI_VERSION = '%version';
EOF
sed -i 's/npm run build:assets && //' packages/cli/package.json
# use system esbuild
ln -sv %_bindir/esbuild .
sed -i "s/0.25.6/$(rpm -q --qf '%{VERSION}' esbuild)/g" node_modules/esbuild/lib/main.js

%build
export ESBUILD_BINARY_PATH=./esbuild
cd packages/cli
npm run build
cd -
node esbuild.config.js

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_libexecdir/%name
install -m 0644 dist/cli.js %buildroot%_libexecdir/%name
install -m 0755 %SOURCE4 %buildroot%_bindir/qwen

%files
%_bindir/qwen
%_libexecdir/%name
%doc LICENSE

%changelog
* Sat Feb 28 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.6-alt1
- Updated to version 0.10.6.

* Wed Feb 18 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.5-alt1
- Updated to version 0.10.5.

* Fri Feb 06 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.1-alt1
- Updated to version 0.9.1.

* Fri Jan 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.2-alt1
- Updated to version 0.7.2.

* Sat Jan 17 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.1-alt1
- Updated to version 0.7.1.

* Sun Dec 28 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.0-alt1
- Updated to version 0.6.0.

* Mon Dec 15 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.0-alt1
- Updated to version 0.5.0.

* Sun Nov 30 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.2-alt2
- Build for all architectures.

* Wed Nov 19 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.2-alt1
- Updated to version 0.2.2.

* Fri Nov 14 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.1-alt1
- Updated to version 0.2.1.

* Fri Nov 07 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.0-alt1
- Updated to version 0.2.0.

* Thu Nov 06 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.4-alt1
- Initial build for ALT.
