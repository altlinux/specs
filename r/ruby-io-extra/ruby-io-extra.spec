%define pkgname io-extra

Name: ruby-%pkgname 
Version: 1.2.2
Release: alt1

Summary: Adds IO.fdwalk, IO.closefrom and IO.directio
Group: Development/Ruby
License: Ruby
Url: http://rubyforge.org/projects/shards

Packager: Anton Gorlov <stalker at altlinux.org>


Source: %pkgname-%version.tar

# Automatically added by buildreq on Thu Aug 11 2011
# optimized out: ruby ruby-stdlibs ruby-tool-rdoc
BuildRequires: libruby-devel ruby-test-unit ruby-tool-setup

%description 
the io-extra library provides a few extra IO methods that you may find
handy. They are IO.closefrom, IO.fdwalk, IO#directio and IO#directio

%package doc 
Summary: Documentation files for %name 
Group: Documentation

%description doc 
Documentation files for %name

%prep
%setup -q -n  %pkgname-%version
%update_setup_rb

%build 
%ruby_config 
%ruby_build


%install 
%ruby_install 
%rdoc ext/

%files 
%doc README CHANGES 
#ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc 
%ruby_ri_sitedir/IO*

%changelog 
* Thu Aug 11 2011 Anton Gorlov <stalker@altlinux.ru> 1.2.2-alt1
- initial build for ALTLinux 




