%define _unpackaged_files_terminate_build 1

Name: opencommit
Version: 3.2.19
Release: alt1

Summary: Auto-generate meaningful commits in a second
License: MIT
Group: Development/Tools
Url: https://www.npmjs.com/package/opencommit
VCS: https://github.com/di-sukharev/opencommit

BuildArch: noarch

Source: %name-%version.tar
Source1: node_modules.tar

Requires: node

BuildRequires: node
BuildRequires: npm
BuildRequires: esbuild

# https://bugzilla.altlinux.org/53408#c40
%filter_from_requires /^\/usr\/bin\/node$/d

%description
Top #1 and most feature rich GPT wrapper for git - generate commit
messages with an LLM in 1 sec - works with Claude, GPT and every other
provider, supports local Ollama models too.

%prep
%setup -a1
npm_esbuild=$(node -p "require('./node_modules/esbuild/package.json').version")
distro_esbuild=%{get_version esbuild}
find node_modules/esbuild -name "*.js" -exec \
    sed -i "s/$npm_esbuild/$distro_esbuild/g" {} +
ln -s %_bindir/esbuild .

%build
# use system esbuild to avoid platform-specific binary
export ESBUILD_BINARY_PATH=./esbuild
npm run build

%install
install -Dm 755 out/cli.cjs %buildroot%_libexecdir/%name/cli.cjs
install -Dm 644 out/tiktoken_bg.wasm \
    %buildroot%_libexecdir/%name/tiktoken_bg.wasm
mkdir -p %buildroot%_bindir
ln -s %_libexecdir/%name/cli.cjs %buildroot%_bindir/%name
ln -s %name %buildroot%_bindir/oco

%check
npm test

%files
%doc README.md
%_bindir/%name
%_bindir/oco
%_libexecdir/%name

%changelog
* Tue May 05 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.2.19-alt1
- Initial build for ALT.

