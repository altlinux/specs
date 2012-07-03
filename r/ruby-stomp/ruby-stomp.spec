# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname stomp

Name: ruby-%pkgname
Version: 1.1.9
Release: alt1

Summary: Ruby client for the Stomp messaging protocol
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/stomp/

Packager: Sergey Alembekov <rt@altlinux.ru>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Wed Sep 28 2011 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-setup

%description
FILL ME.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%ruby_sitelibdir/*

%changelog
* Wed Sep 28 2011 Sergey Alembekov <rt@altlinux.ru> 1.1.9-alt1
- Built for Sisyphus

