%define  pkgname minitar

Name:    ruby-%pkgname
Version: 0.6.1
Release: alt1

Summary: Minimal pure-ruby support for POSIX tar(1) archives.
License: Simplified BSD/Ruby
Group:   Development/Ruby
Url:     https://github.com/halostatue/minitar/

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
The minitar library is a pure-Ruby library that provides the ability to deal with
POSIX tar(1) archive files.

This is release 0.6, providing a number of bug fixes including a directory
traversal vulnerability, CVE-2016-10173. This release starts the migration and
modernization of the code:

* the licence has been changed to match the modern Ruby licensing scheme (Ruby
  and Simplified BSD instead of Ruby and GNU GPL);
* the minitar command-line program has been separated into the minitar-cli gem;
* the archive-tar-minitar gem now points to the minitar and minitar-cli gems
  and discourages its installation.

Some of these changes may break existing programs that depend on the internal
structure of the minitar library, but every effort has been made to ensure
compatibility; inasmuch as is possible, this compatibility will be maintained
through the release of minitar 1.0 (which will have strong breaking changes).

minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernandez Pradier for the rpa-base project.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

#%check
#%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
