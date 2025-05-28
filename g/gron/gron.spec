%define _unpackaged_files_terminate_build 1

%global import_path github.com/tomnomnom/gron
Name: gron
Version: 0.7.1
Release: alt1

Summary: tool to transform JSON into discrete, greppable assignments
License: MIT
Group: Development/Other
Url: https://github.com/tomnomnom/gron

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
gron transforms JSON into discrete assignments to make it easier to grep
for what you want and see the absolute 'path' to it. gron can read JSON
from a local file, over the network, or directly from STDIN.

gron eases the exploration of APIs that return large blobs of JSON but 
have terrible documentation.

gron can work backwards too, enabling you to turn your filtered data 
back into JSON.

%prep
%setup -a1
%patch -p1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name

%files
%doc LICENSE docs *.mkd
%_bindir/*

%changelog
* Wed May 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus
