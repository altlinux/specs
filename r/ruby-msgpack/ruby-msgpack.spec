%define  pkgname msgpack

Name: 	 ruby-%pkgname
Version: 1.1.0
Release: alt1.3

Summary: MessagePack implementation for Ruby
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/msgpack/msgpack-ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

%filter_from_requires /^ruby(java)$/d; \!^ruby(msgpack/msgpack\.jar)$!d

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup libruby-devel

%description
MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON but it's faster and smaller. For
example, small integers (like flags or error code) are encoded into a single
byte, and typical short strings only require an extra byte in addition to the
strings themselves.

If you ever wished to use JSON for convenience (storing an image with metadata)
but could not for technical reasons (binary data, size, speed ...), MessagePack
is a perfect replacement.

%package doc
Summary: Documentation files for %name
Group: Documentation


%description doc
Documentation files for %{name}.

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

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.1.0-alt1
- Initial build in Sisyphus
