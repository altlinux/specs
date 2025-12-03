%global _unpackaged_files_terminate_build 1
# git rev-parse --short v%version
%global commit_hash 578c49741

Name: gemini-cli
Version: 0.19.1
Release: alt1
Summary: AI agent that brings the power of Gemini directly into your terminal
License: Apache-2.0
Group: Development/Tools
Url: https://geminicli.com
VCS: https://github.com/google-gemini/gemini-cli

Source: %name-%version.tar
Source1: node_modules.tar
Source2: node_modules_cli.tar
Source3: node_modules_core.tar
Source4: node_modules_a2a.tar
Source5: gemini.sh

BuildArch: noarch

BuildRequires: esbuild
BuildRequires: npm

%description
Gemini CLI is an open-source AI agent that brings the power of Gemini
directly into your terminal. It provides lightweight access to Gemini,
giving you the most direct path from your prompt to our model.

%prep
# npm install
# git add -f node_modules packages/{cli,core,a2a-server}/node_modules
# git commit -m "Updated node modules." --no-verify
%setup -a 1 -a 2 -a 3 -a 4
mkdir -p packages/{core,cli}/src/generated
tee packages/{core,cli}/src/generated/git-commit.{js,ts} <<EOF
export const GIT_COMMIT_INFO = '%commit_hash';
export const CLI_VERSION = '%version';
EOF
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
mkdir -p %buildroot%_bindir %buildroot%_libexecdir/%name
install -m 0644 bundle/gemini.js %buildroot%_libexecdir/%name
install -m 0755 %SOURCE5 %buildroot%_bindir/gemini

%files
%_bindir/gemini
%_libexecdir/%name
%doc LICENSE

%changelog
* Wed Dec 03 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.19.1-alt1
- Updated to version 0.19.1.

* Sun Nov 30 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.18.3-alt1
- Initial build for ALT.
