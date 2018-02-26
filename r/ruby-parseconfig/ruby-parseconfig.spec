# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define pkgname parseconfig

Name: ruby-%pkgname
Version: 0.5
Release: %branch_release alt1

Summary: ParseConfig provides simple parsing of standard *nix style config files.
Group: Development/Ruby
License: %gpl3only
Url: http://rubyforge.org/projects/%pkgname

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
# Automatically added by buildreq on Sun Sep 32 3001 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
rb-parseconfig is a Ruby class written to parse simple configuration
files in the format of 'param = value'. The key benefit is that your
ruby scripts can use the same configuration files of most unix/linux
applications.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc README CREDITS Changelog LICENSE demo.*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Feb 25 2010 Aleksey Avdeev <solo@altlinux.ru> 0.5-alt1
- initial build for ALT Linux Sisyphus
