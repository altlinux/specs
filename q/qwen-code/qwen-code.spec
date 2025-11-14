%global _unpackaged_files_terminate_build 1
# git rev-parse --short v%version
%global commit_hash 7a472e4fc

Name: qwen-code
Version: 0.2.1
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

ExclusiveArch: x86_64

BuildRequires: npm

%description
QwenCode is a powerful command-line AI workflow tool adapted
from Gemini CLI, specifically optimized for Qwen3-Coder models.
It enhances your development workflow with advanced code
understanding, automated tasks, and intelligent assistance.

%prep
# npm ci
# git add -f node_modules packages/cli/node_modules packages/core/node_modules
# git commit -m "Updated node modules." --no-verify
%setup -a 1 -a 2 -a 3
mkdir -p packages/{core,cli}/src/generated
tee packages/{core,cli}/src/generated/git-commit.{js,ts} <<EOF
export const GIT_COMMIT_INFO = '%commit_hash';
export const CLI_VERSION = '%version';
EOF

%build
cd packages/cli
npm run build
cd -
node esbuild.config.js

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_libexecdir/%name/node_modules
cp -r node_modules/tiktoken %buildroot%_libexecdir/%name/node_modules
install -m 0644 dist/cli.js %buildroot%_libexecdir/%name
install -m 0755 %SOURCE4 %buildroot%_bindir/qwen

%files
%_bindir/qwen
%_libexecdir/%name
%doc LICENSE

%changelog
* Fri Nov 14 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.1-alt1
- Updated to version 0.2.1.

* Fri Nov 07 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.0-alt1
- Updated to version 0.2.0.

* Thu Nov 06 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.4-alt1
- Initial build for ALT.
