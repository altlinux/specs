%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name dbus
%define f_pkg_name dbus
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.10.4
Release: alt1
License: GPL-3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: https://john-millikin.com/software/haskell-dbus/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A client library for the D-Bus IPC system.



# Automatically added by buildreq on Mon Dec 24 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-mtl ghc7.6.1-parsec ghc7.6.1-primitive ghc7.6.1-text ghc7.6.1-transformers ghc7.6.1-xml-types libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cereal ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-libxml-sax ghc7.6.1-network ghc7.6.1-random ghc7.6.1-vector libxml2-devel

%description
D-Bus is a simple, message-based protocol for inter-process communication,
which allows applications to interact with other parts of the machine and
the user's session using remote procedure calls.

D-Bus is a essential part of the modern Linux desktop, where it replaces
earlier protocols such as CORBA and DCOP.

This library is an implementation of the D-Bus protocol in Haskell. It can
be used to add D-Bus support to Haskell applications, without the awkward
interfaces common to foreign bindings.

Example: connect to the session bus, and get a list of active names.

@ &#x7b;-\# LANGUAGE OverloadedStrings \#-&#x7d;

import Data.List (sort) import DBus import DBus.Client

main = do &#x20; client <- connectSession &#x20; // &#x20; \-- Request a
list of connected clients from the bus &#x20; reply <- call_ client
(methodCall \"\/org\/freedesktop\/DBus\" \"org.freedesktop.DBus\"
\"ListNames\") &#x20; &#x7b; methodCallDestination = Just
\"org.freedesktop.DBus\" &#x20; &#x7d; &#x20; // &#x20; \--
org.freedesktop.DBus.ListNames() returns a single value, which is &#x20;
\-- a list of names (here represented as [String]) &#x20; let Just names =
fromVariant (methodReturnBody reply !! 0) &#x20; // &#x20; \-- Print each
name on a line, sorted so reserved names are below &#x20; \-- temporary
names. &#x20; mapM_ putStrLn (sort names) @

>$ ghc --make list-names.hs >$ ./list-names >:1.0 >:1.1 >:1.10 >:1.106
>:1.109 >:1.110 >ca.desrt.dconf >org.freedesktop.DBus
>org.freedesktop.Notifications >org.freedesktop.secrets
>org.gnome.ScreenSaver

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Mon Dec 24 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10.4-alt1
- Spec created by cabal2rpm 0.20_08
