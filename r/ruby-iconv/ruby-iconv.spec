%define bname iconv
Name: ruby-%bname
Version: 1.0
Release: alt1
Summary: Ruby iconv module
License: Ruby
Group: Development/Ruby
URL: http://www.ruby-lang.org/
Source: %name-%version.tar
Conflicts: rubu-stdlibs <= 1.9.3
Requires: ruby-stdlibs

BuildPreReq: rpm-build-ruby
BuildRequires: ruby libruby-devel

%description
This package contains deprecated Ruby iconv module.


%prep
%setup -q


%build
%make_build CFLAGS="%optflags" RUBY=%__ruby


%install
%makeinstall_std RUBY_ARCHDIR=%ruby_sitearchdir


%files
%ruby_sitearchdir/*


%changelog
* Fri Mar 21 2014 Led <led@altlinux.ru> 1.0-alt1
- initial build
