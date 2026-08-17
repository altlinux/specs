%define _unpackaged_files_terminate_build 1
%global import_path github.com/betterleaks/betterleaks

Name: betterleaks
Version: 1.7.4
Release: alt1
Summary: A Better Secrets Scanner built for configurability and speed
License: MIT
Group: Development/Tools
Url: https://betterleaks.com/
Vcs: https://github.com/betterleaks/betterleaks

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Betterleaks is a tool for detecting secrets like passwords, API keys, and tokens
in git repos, files, and whatever else you wanna throw at it via stdin.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
%golang_prepare
%golang_build .

for file in $(find -name "*\[generated\]*"); do
    mv -v "$file" "${file//\[generated\]/}"
done

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d

"$BUILDDIR/bin/betterleaks" completion bash > \
            %buildroot%_datadir/bash-completion/completions/betterleaks
"$BUILDDIR/bin/betterleaks" completion zsh > \
            %buildroot%_datadir/zsh/site-functions/_betterleaks
"$BUILDDIR/bin/betterleaks" completion fish > \
            %buildroot%_datadir/fish/vendor_completions.d/betterleaks.fish

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/bash-completion/completions/betterleaks
%_datadir/zsh/site-functions/_betterleaks
%_datadir/fish/vendor_completions.d/betterleaks.fish


%changelog
* Mon Aug 17 2026 Egor Ignatov <egori@altlinux.org> 1.7.4-alt1
- New version 1.7.4.

* Fri Jul 17 2026 Egor Ignatov <egori@altlinux.org> 1.6.1-alt1
- New version 1.6.1.

* Fri Jun 05 2026 Vladislav Glinkin <smasher@altlinux.org> 1.4.0-alt1
- New version

* Thu May 28 2026 Vladislav Glinkin <smasher@altlinux.org> 1.3.1-alt1
- New version

* Tue Mar 24 2026 Vladislav Glinkin <smasher@altlinux.org> 1.1.1-alt1
- Initial build for ALT

