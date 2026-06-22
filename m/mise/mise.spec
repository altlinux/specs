%define _unpackaged_files_terminate_build 1

%def_with check

Name: mise
Version: 2026.6.12
Release: alt1

Summary: The front-end to your dev env
License: MIT
Group: Development/Tools
Url: https://mise.jdx.dev
VCS: https://github.com/jdx/mise

# rustc: memory allocation failure during mise linking
ExcludeArch: %ix86

Source: %name-%version.tar
Source1: vendor.tar

Requires: usage
Requires: libatomic1

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(openssl)
BuildRequires: cmake
BuildRequires: clang-devel

%if_with check
BuildRequires: git
%endif

%description
mise (pronounced "meez") or "mise-en-place" is a development environment
setup tool. The name refers to a French culinary phrase that roughly
translates to "setup" or "put in place". The idea is that before one
begins cooking, they should have all their utensils and ingredients
ready to go in their place.

mise does the same for your projects. Using its mise.toml config file,
you'll have a consistent way to setup and interact with your projects no
matter what language they're written in.

Its functionality is grouped into 3 categories described below.

mise installs and manages dev tools/runtimes like node, python, or
terraform both simplifying installing these tools and allowing you to
specify which version of these tools to use in different projects. mise
supports hundreds of dev tools.

mise manages environment variables letting you specify configuration
like AWS_ACCESS_KEY_ID that may differ between projects. It can also be
used to automatically activate a Python virtualenv when entering
projects too.

mise is a task runner that can be used to share common tasks within a
project among developers and make things like running tasks on file
changes easy.

%prep
%setup -a1
%rust_prep

%build
%rust_build
./target/release/%name completion bash > %name.bash
./target/release/%name completion fish > %name.fish
./target/release/%name completion zsh > %name.zsh

%install
%rust_install
install -Dm 644 man/man1/%name.1 %buildroot%_man1dir/%name.1
install -Dm 644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name

# disable mise self update
install -Dm 644 /dev/null %buildroot%_libexecdir/%name/.disable-self-update

%check
%rust_test

%files
%doc CHANGELOG.md CONTRIBUTING.md README.md SECURITY.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_libexecdir/%name
%_man1dir/%name.1.*

%changelog
* Mon Jun 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.6.12-alt1
- Updated to version 2026.6.12.
- Added libatomic1 to requires (Closes: #58938).

* Mon May 18 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.5.11-alt1
- Updated to version 2026.5.11.

* Thu Apr 30 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.4.27-alt1
- Updated to version 2026.4.27.

* Thu Apr 09 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2026.4.5-alt1
- Initial build for ALT.

