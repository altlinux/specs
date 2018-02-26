# Required parameters:
#   %func - the plugin name
#   %builddeps - this line will be appended to BuildRequires (gmpc-devel is
#     already there)

# Using this meta-spec:
# - %define the required parameters,
# - put correct Name:, Version:, and License: tags
# - put BuildRequires(pre): rpm-build-gmpc
# - %include this file;
# - append %files section;
# - append %changelog section.
# That's all folks!

%define _unpackaged_files_terminate_build 1

%define prog_name gmpc
%define part plugin

Summary: %func %part for %prog_name
License: %gpl2plus
Group: Sound

Url: http://www.sarine.nl/gmpc-plugins

Source: %prog_name-%part-%func-%version.tar

#Requires:	%prog_name
BuildRequires(pre): rpm-build-licenses
BuildRequires: libmpd-devel gmpc-devel %builddeps

%description
%func %part for %prog_name.

%prep
%setup -q -n %prog_name-%part-%func-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

