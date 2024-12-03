%define _unpackaged_files_terminate_build 1

Name: binsider
Version: 0.1.0
Release: alt1
Summary: Contextual, dynamic aliases for the bash shell.
License: Apache-2.0 and MIT 
Group: Development/Ruby
Url: https://github.com/sebglazebrook/aliases
ExclusiveArch: x86_64

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
Dynamic aliases based on the directory you are currently in.
Ever wanted to type something like server in whole bunch of different
directories and your computer just knows what you're thinking?
Now you can!

%prep
%setup

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%rust_build

%install
%rust_install

%files
%doc README.md LICENSE-*
%_bindir/%name

%changelog
* Fri Sep 06 2024 Pavel Shilov <zerospirit@altlinux.org> 0.1.0-alt1
- initial build for Sisyphus
