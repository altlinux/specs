%define        pkgname em-mongo

Name: 	       ruby-%pkgname
Version:       0.6.0
Release:       alt2
Summary:       EventMachine MongoDB Driver (based off of RMongo)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bcg/em-mongo
# VCS:         https://github.com/bcg/em-mongo.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
%gem_replace_version bson ~> 4.0
BuildRequires(pre): rpm-build-ruby

%description
An EventMachine client for MongoDB. Originally based on RMongo, this client aims
to be as api compatible with mongo-ruby-driver as possible.

For methods that do not retrieve data from the database the api of em-mongo
should be identical (though a subset) to the mongo-ruby-driver. This includes
the various update methods like insert, save and update (without the :safe flag,
which is handled separately) as well as find, which returns a cursor.

For operations that require IO, em-mongo always returns an EventMachine
deferrable.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir/*

%files         doc
%ruby_gemdocdir/*

%changelog
* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt2
- Use Ruby Policy 2.0.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- New version.

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.1-alt1
- New version

* Wed Oct 18 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
