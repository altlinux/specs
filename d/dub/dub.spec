%define _unpackaged_files_terminate_build 1

# follow architectures of D compiler
ExclusiveArch: %ix86 x86_64

Name: dub
Version: 1.38.1
Release: alt1
Summary: Package and build management system for D
Group: Development/Other
License: MIT
Url: https://dlang.org/
VCS: https://github.com/dlang/dub.git

# https://github.com/dlang/dub.git
Source: %name-%version.tar

BuildRequires: dmd

%description
DUB emerged as a more general replacement for vibe.d's package manager.
It does not imply a dependency to vibe.d for packages and was extended
to not only directly build projects, but also to generate project files
(currently VisualD). Mono-D also supports the use of
dub.json (dub's package description) as the project file.

The project's philosophy is to keep things as simple as possible.
All that is needed to make a project a dub package is to write
a short dub.json file and put the source code into a source subfolder.
It can then be registered on the public package registry
to be made available for everyone. Any dependencies specified in dub.json
are automatically downloaded and made available to the project during
the build process.

Key features:
* Simple package and build description not getting in your way
* Integrated with Git, avoiding maintenance tasks such as incrementing
  version numbers or uploading new project releases
* Generates VisualD project/solution files, integrated into MonoD
* Support for DMD, GDC and LDC (common DMD flags are translated automatically)
* Supports development workflows by optionally using local directories
  as a package source

%prep
%setup

%build
dmd -run build.d

%install
install -Dm755 bin/dub %buildroot%_bindir/dub

%files
%doc LICENSE
%doc ARCHITECTURE.md CONTRIBUTING.md README.md
%_bindir/dub

%changelog
* Tue Sep 03 2024 Andrey Kovalev <ded@altlinux.org> 1.38.1-alt1
- Updated to upstream version 1.38.1.

* Wed Mar 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.24.1-alt1
- Updated to upstream version 1.24.1.

* Fri Oct 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.23.0-alt1
- Initial build for ALT (ALT #39060).
