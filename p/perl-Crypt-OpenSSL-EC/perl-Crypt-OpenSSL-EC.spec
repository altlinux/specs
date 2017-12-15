%define _unpackaged_files_terminate_build 1
%define module_name Crypt-OpenSSL-EC
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel libssl-devel perl(AutoLoader.pm) perl(Config.pm) perl(Crypt/OpenSSL/Bignum.pm) perl(Crypt/OpenSSL/Bignum/CTX.pm) perl(Exporter.pm) perl(ExtUtils/Constant.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.31
Release: alt1.1
Summary: Perl extension for OpenSSL EC (Elliptic Curves) library
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MI/MIKEM/%{module_name}-%{version}.tar.gz

%description
This module provides a standard (non-OO) interface to the OpenSSL EC (Elliptic Curve) library.
Some OO Calls are supported.

Most of the functions described in openssl/ec.h are supported.

It provides the Crypt::OpenSSL::EC class which defines some high level functions and constants.
At also provides 4 other classes for managing EC objects:

=over 4

=item Crypt::OpenSSL::EC::EC_GROUP

=item Crypt::OpenSSL::EC::EC_POINT

=item Crypt::OpenSSL::EC::EC_KEY

=item Crypt::OpenSSL::EC::EC_METHOD

=back

All objects created by these 4 classes are implemented as blessed Perl mortal
references.  This ensures they will be auto-destroyed when the Perl variable
becomes unreferenced. ASlo the approproae EC free function wil be called to
free the underlying EC object.

Further, it means that many of the functions below can be called using O-O
methods.  If a method's first argument is the same as the class the method is
in, then it can be called O-O style. For example the following 2 calls are
equivalent:

=over 4

=item my $newgroup = Crypt::OpenSSL::EC::EC_GROUP::dup($group);

=item my $newgroup = $group->dup();

=back

=over 4

=item Crypt::OpenSSL::EC::EC_GFp_simple_method();

Returns the basic GFp ec methods which provides the basis for the
optimized methods. 

=item Crypt::OpenSSL::EC::EC_GFp_mont_method();

Returns GFp methods using montgomery multiplication.

=item Crypt::OpenSSL::EC::EC_GFp_nist_method();

Returns GFp methods using optimized methods for NIST recommended curves

=item Crypt::OpenSSL::EC::EC_GF2m_simple_method();

Returns the basic GF2m ec method 

=item Crypt::OpenSSL::EC::EC_GROUP::new($method);

Creates a new EC_GROUP object
$method is the method to use

=item Crypt::OpenSSL::EC::EC_GROUP::set_curve_GFp($group, $p, $a, $b, $ctx);

Sets the parameter of a ec over GFp defined by y^2 = x^3 + a*x + b
  group  EC_GROUP object
  p      BIGNUM with the prime number
  a      BIGNUM with parameter a of the equation
  b      BIGNUM with parameter b of the equation
  ctx    BN_CTX object (optional)
 return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_GROUP::method_of($group);

Returns the EC_METHOD of the EC_GROUP object.

=item Crypt::OpenSSL::EC::EC_METHOD::get_field_type($method)

Returns the field type of the EC_METHOD.

=item Crypt::OpenSSL::EC::EC_GROUP::copy($dst, $src);

Copies EC_GROUP objects. Note: both EC_GROUPs must use the same EC_METHOD.
return newly created EC_GROUP object or NULL in case of an error.

=item Crypt::OpenSSL::EC::EC_GROUP::dup($src);

Creates a new EC_GROUP object and copies the copies the content
form src to the newly created EC_GROUP object.
return newly created EC_GROUP object or NULL in case of an error.

=item Crypt::OpenSSL::EC::EC_GROUP::get_curve_GFp($group, $p, $a, $b, $ctx);

Gets the parameter of the ec over GFp defined by y^2 = x^3 + a*x + b
  group  EC_GROUP object
  p      BIGNUM for the prime number
  a      BIGNUM for parameter a of the equation
  b      BIGNUM for parameter b of the equation
  ctx    BN_CTX object (optional)
 return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_GROUP::set_curve_GF2m($group, $p, $a, $b, $ctx);

Sets the parameter of a ec over GF2m defined by y^2 + x*y = x^3 + a*x^2 + b
  group  EC_GROUP object
  p      BIGNUM with the polynomial defining the underlying field
  a      BIGNUM with parameter a of the equation
  b      BIGNUM with parameter b of the equation
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_GROUP::get_curve_GF2m($group, $p, $a, $b, $ctx);

Gets the parameter of the ec over GF2m defined by y^2 + x*y = x^3 + a*x^2 + b
  group  EC_GROUP object
  p      BIGNUM for the polynomial defining the underlying field
  a      BIGNUM for parameter a of the equation
  b      BIGNUM for parameter b of the equation
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured


=item Crypt::OpenSSL::EC::print_errs();

=item Crypt::OpenSSL::EC::EC_POINT::new($group);

Creates a new EC_POINT object for the specified EC_GROUP
  group  EC_GROUP the underlying EC_GROUP object
  return newly created EC_POINT object or NULL if an error occurred

=item Crypt::OpenSSL::EC::EC_POINT::free($point);

Frees a EC_POINT object
  point  EC_POINT object to be freed
This should normally not be called from Perl, since EC_POINT objects created by this 
library are auto-destroyed when they become unreferenced.

=item Crypt::OpenSSL::EC::EC_POINT::clear_free($point);

Clears and frees a EC_POINT object
  point  EC_POINT object to be cleared and freed
This should normally not be called from Perl, since EC_POINT objects created by this 
library are auto-destroyed when they become unreferenced.


=item Crypt::OpenSSL::EC::EC_POINT::copy($dst, $src);

Copies EC_POINT object
  dst  destination EC_POINT object
  src  source EC_POINT object
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::dup($src, $group);

Creates a new EC_POINT object and copies the content of the supplied
EC_POINT
  src    source EC_POINT object
  group  underlying the EC_GROUP object
  return newly created EC_POINT object or NULL if an error occurred 

=item Crypt::OpenSSL::EC::EC_POINT::set_to_infinity($group, $point);

Sets a point to infinity (neutral element)
  group  underlying EC_GROUP object
  point  EC_POINT to set to infinity
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::get_Jprojective_coordinates_GFp($group, $p, $x, $y, $z, $ctx);

Gets the jacobian projective coordinates of a EC_POINT over GFp
  group  underlying EC_GROUP object
  p      EC_POINT object
  x      BIGNUM for the x-coordinate
  y      BIGNUM for the y-coordinate
  z      BIGNUM for the z-coordinate
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::set_affine_coordinates_GFp($group, $p, $x, $y, $ctx);

Sets the affine coordinates of a EC_POINT over GFp
  group  underlying EC_GROUP object
  p      EC_POINT object
  x      BIGNUM with the x-coordinate
  y      BIGNUM with the y-coordinate
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::get_affine_coordinates_GFp($group, $p, $x, $y, $ctx);

Gets the affine coordinates of a EC_POINT over GFp
  group  underlying EC_GROUP object
  p      EC_POINT object
  x      BIGNUM for the x-coordinate
  y      BIGNUM for the y-coordinate
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::set_compressed_coordinates_GFp($group, $p, $x, $y_bit, $ctx);

Sets the x9.62 compressed coordinates of a EC_POINT over GFp
  group  underlying EC_GROUP object
  p      EC_POINT object
  x      BIGNUM with x-coordinate
  y_bit  integer with the y-Bit (either 0 or 1)
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::set_affine_coordinates_GF2m($group, $p, $x, $y, $ctx);

Sets the affine coordinates of a EC_POINT over GF2m
  group  underlying EC_GROUP object
  p      EC_POINT object
  x      BIGNUM with the x-coordinate
  y      BIGNUM with the y-coordinate
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::get_affine_coordinates_GF2m($group, $p, $x, $y, $ctx);

Gets the affine coordinates of a EC_POINT over GF2m
  group  underlying EC_GROUP object
  p      EC_POINT object
  x      BIGNUM for the x-coordinate
  y      BIGNUM for the y-coordinate
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::set_compressed_coordinates_GF2m($group, $p, $x, $y_bit, $ctx);

Sets the x9.62 compressed coordinates of a EC_POINT over GF2m
  group  underlying EC_GROUP object
  p      EC_POINT object
  x      BIGNUM with x-coordinate
  y_bit  integer with the y-Bit (either 0 or 1)
  ctx    BN_CTX object (optional)
  \return 1 on success and 0 if an error occured


=item Crypt::OpenSSL::EC::EC_POINT::is_at_infinity($group, $p);

Checks whether the point is the neutral element of the group
  group  the underlying EC_GROUP object
  p      EC_POINT object
  return 1 if the point is the neutral element and 0 otherwise

=item Crypt::OpenSSL::EC::EC_POINT::point2oct($group, $p, $form, $ctx);

Encodes a EC_POINT object to a octet string
  group  underlying EC_GROUP object
  p      EC_POINT object
  form   point conversion form
  ctx    BN_CTX object (optional)
  return the encoded EC point

=item Crypt::OpenSSL::EC::EC_POINT::oct2point($group, $p, $buf, $ctx);

Decodes a EC_POINT from a octet string
  group  underlying EC_GROUP object
  p      EC_POINT object
  buf    buffer with the encoded ec point
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::point2bn($group, $p, $form, $bn, $ctx);

=item Crypt::OpenSSL::EC::EC_POINT::bn2point($group, $bn, $p, $ctx);

=item Crypt::OpenSSL::EC::EC_POINT::point2hex($group, $p, $form, $bn, $ctx);

=item Crypt::OpenSSL::EC::EC_POINT::hex2point($group, $bn, $p, $ctx);


=item Crypt::OpenSSL::EC::EC_POINT::add($group, $r, $a, $b, $ctx);

 Computes the sum of two EC_POINT 
  group  underlying EC_GROUP object
  r      EC_POINT object for the result (r = a + b)
  a      EC_POINT object with the first summand
  b      EC_POINT object with the second summand
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::dbl($group, $r, $a, $ctx);

Computes the double of a EC_POINT
  group  underlying EC_GROUP object
  r      EC_POINT object for the result (r = 2 * a)
  a      EC_POINT object 
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::invert($group, $a, $ctx);

Computes the inverse of a EC_POINT
  group  underlying EC_GROUP object
  a      EC_POINT object to be inverted (it's used for the result as well)
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_POINT::is_on_curve($group, $point, $ctx));

Checks whether the point is on the curve 
  group  underlying EC_GROUP object
  point  EC_POINT object to check
  ctx    BN_CTX object (optional)
  return 1 if point if on the curve and 0 otherwise

=item Crypt::OpenSSL::EC::EC_POINT::cmp($group, $a, $b, $ctx);

Compares two EC_POINTs 
  group  underlying EC_GROUP object
  a      first EC_POINT object
  b      second EC_POINT object
  ctx    BN_CTX object (optional)
  return 0 if both points are equal and a value != 0 otherwise

=item Crypt::OpenSSL::EC::EC_POINT::make_affine($group, $point, $ct);

=item Crypt::OpenSSL::EC::EC_POINTs::make_affine

Not Implemented

=item Crypt::OpenSSL::EC::EC_POINTs::mul

Not Implemented

=item    Crypt::OpenSSL::EC::EC_GROUP::set_generator($group, $generator, $order, $cofactor);

Sets the generator and it's order/cofactor of a EC_GROUP object.
  group      EC_GROUP object 
  generator  EC_POINT object with the generator.
  order      the order of the group generated by the generator.
  cofactor   the index of the sub-group generated by the generator
           in the group of all points on the elliptic curve.
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_GROUP::get0_generator($group);

Returns the generator of a EC_GROUP object.

  group  EC_GROUP object

return the currently used generator (possibly NULL).

=item Crypt::OpenSSL::EC::EC_GROUP::get_degree($group)

Returns the number of bits needed to represent a field element 
  group  EC_GROUP object
  return number of bits needed to represent a field element

=item Crypt::OpenSSL::EC::EC_GROUP::check($group, $ctx);

Checks whether the parameter in the EC_GROUP define a valid ec group
  group  EC_GROUP object
  ctx    BN_CTX object (optional)
  return 1 if group is a valid ec group and 0 otherwise

=item  Crypt::OpenSSL::EC::EC_GROUP::check_discriminant($group, $ctx);

Checks whether the discriminant of the elliptic curve is zero or not
  group  EC_GROUP object
  ctx    BN_CTX object (optional)
  return 1 if the discriminant is not zero and 0 otherwise

=item  Crypt::OpenSSL::EC:: EC_GROUP::cmp($a, $b, $ctx);

Compares two EC_GROUP objects
  a    first EC_GROUP object
  b    second EC_GROUP object
  ctx  BN_CTX object (optional)
  return 0 if both groups are equal and 1 otherwise

=item Crypt::OpenSSL::EC::EC::EC_GROUP::new_curve_GFp($p, $a, $b, $ctx);

Creates a new EC_GROUP object with the specified parameters defined
over GFp (defined by the equation y^2 = x^3 + a*x + b)
  p    BIGNUM with the prime number
  a    BIGNUM with the parameter a of the equation
  b    BIGNUM with the parameter b of the equation
  ctx  BN_CTX object (optional)
  return newly created EC_GROUP object with the specified parameters

=item Crypt::OpenSSL::EC::EC_GROUP::new_curve_GF2m($p, $a, $b, $ctx);

Creates a new EC_GROUP object with the specified parameters defined
over GF2m (defined by the equation y^2 + x*y = x^3 + a*x^2 + b)
  p    BIGNUM with the polynomial defining the underlying field
  a    BIGNUM with the parameter a of the equation
  b    BIGNUM with the parameter b of the equation
  ctx  BN_CTX object (optional)
  return newly created EC_GROUP object with the specified parameters

=item Crypt::OpenSSL::EC::EC_GROUP::new_by_curve_name($nid);

Creates a EC_GROUP object with a curve specified by a NID
  nid  NID of the OID of the curve name
  return newly created EC_GROUP object with specified curve or NULL
           if an error occurred

=item Crypt::OpenSSL::EC::EC_get_builtin_curves($r, $nitems);

EC_builtin_curves(EC_builtin_curve *r, size_t size) returns number 
of all available curves or zero if a error occurred. 
In case r ist not zero nitems EC_builtin_curve structures 
are filled with the data of the first nitems internal groups


=item Crypt::OpenSSL::EC::EC_GROUP::get_order($group, $order, $ctx);

Gets the order of a EC_GROUP

  group  EC_GROUP object
  order  BIGNUM to which the order is copied
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_GROUP::get_cofactor($group, $cofactopr, $ctx)

Gets the cofactor of a EC_GROUP

  group     EC_GROUP object
  cofactor  BIGNUM to which the cofactor is copied
  ctx       BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item Crypt::OpenSSL::EC::EC_GROUP::set_curve_name($group, $nid);

Sets the name of a EC_GROUP object
  group  EC_GROUP object
  nid    NID of the curve name OID

=item Crypt::OpenSSL::EC::EC_GROUP::get_curve_name($group);

Returns the curve name of a EC_GROUP object
  group  EC_GROUP object
  return NID of the curve name OID or 0 if not set.

=item Crypt::OpenSSL::EC::EC_GROUP::set_asn1_flag($group, $flag);

Sets the ASN flag for the group

=item Crypt::OpenSSL::EC::EC_GROUP::get_asn1_flag($group);

Returns the ASN flag for the group

=item    Crypt::OpenSSL::EC::EC_GROUP::set_point_conversion_form($group, $form);

Sets the point conversion form.

=item    Crypt::OpenSSL::EC::EC_GROUP::get_point_conversion_form($group);

Retuns the point conversion for for the group

=item    Crypt::OpenSSL::EC::EC_GROUP::get0_seed($group);

Returns the 0 seed

=item    Crypt::OpenSSL::EC::EC_GROUP::get_seed_len($group);

Returns the seed length

=item    Crypt::OpenSSL::EC::EC_GROUP::set_seed($group, $seed);

Sets the group seed

=item    Crypt::OpenSSL::EC::EC_POINT::mul($group, $r, $n, $q, $m, $ctx));

Computes r = generator * n + q * m
  group  underlying EC_GROUP object
  r      EC_POINT object for the result
  n      BIGNUM with the multiplier for the group generator (optional)
  q      EC_POINT object with the first factor of the second summand
  m      BIGNUM with the second factor of the second summand
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item    Crypt::OpenSSL::EC::EC_GROUP::precompute_mult($group, $ctx);

Stores multiples of generator for faster point multiplication
  group  EC_GROUP object
  ctx    BN_CTX object (optional)
  return 1 on success and 0 if an error occured

=item    Crypt::OpenSSL::EC::EC_GROUP::have_precompute_mult($group);

Reports whether a precomputation has been done
  group  EC_GROUP object
  return 1 if a pre-computation has been done and 0 otherwise

=item    Crypt::OpenSSL::EC::EC_GROUP::get_basis_type($group);

EC_GROUP_get_basis_type() returns the NID of the basis type
used to represent the field elements 

=item    Crypt::OpenSSL::EC::EC_GROUP::get_trinomial_basis($group, $k);

=item    Crypt::OpenSSL::EC:: EC_GROUP::get_pentanomial_basis($group, $k1, $k2, $k3);

=item    Crypt::OpenSSL::EC::EC_GROUP::free($group);

Frees a EC_GROUP object.
This should normally not be called from Perl, since EC_GROUP objects created by this 
library are auto-destroyed when they become unreferenced.

=item    Crypt::OpenSSL::EC::EC_GROUP::clear_free($group);

Clears and frees a EC_GROUP object
This should normally not be called from Perl, since EC_GROUP objects created by this 
library are auto-destroyed when they become unreferenced.

=item Crypt::OpenSSL::EC::EC_KEY::new();
Creates a new EC_KEY object.
 return EC_KEY object or NULL if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::new_by_curve_name($nid);

Creates a new EC_KEY object using a named curve as underlying
EC_GROUP object.
  nid  NID of the named curve.
  return EC_KEY object or NULL if an error occurred. 

=item Crypt::OpenSSL::EC::EC_KEY::free($key);

Frees a EC_KEY object.
  key  EC_KEY object to be freed.
This should normally not be called from Perl, since EC_KEY objects created by this 
library are auto-destroyed when they become unreferenced.

=item Crypt::OpenSSL::EC::EC_KEY::copy($dst, $src);

Copies a EC_KEY object.
  dst  destination EC_KEY object
  src  src EC_KEY object
  return dst or NULL if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::dup($src);

Creates a new EC_KEY object and copies the content from src to it.
  src  the source EC_KEY object
  return newly created EC_KEY object or NULL if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::up_ref($key);

Increases the internal reference count of a EC_KEY object.
  key  EC_KEY object
  return 1 on success and 0 if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::get0_group($key);

Returns the EC_GROUP object of a EC_KEY object
  key  EC_KEY object
  \return the EC_GROUP object (possibly NULL).

=item Crypt::OpenSSL::EC::EC_KEY::set_group($key, $group);

Sets the EC_GROUP of a EC_KEY object.
  key    EC_KEY object
  group  EC_GROUP to use in the EC_KEY object (note: the EC_KEY
         object will use an own copy of the EC_GROUP).
  return 1 on success and 0 if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::set_private_key($key, $prv);

Sets the private key of a EC_KEY object.
  key  EC_KEY object
  prv  BIGNUM with the private key (note: the EC_KEY object
       will use an own copy of the BIGNUM).
  return 1 on success and 0 if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::get0_public_key($key);

Returns the public key of a EC_KEY object.
  key  the EC_KEY object
  return a EC_POINT object with the public key (possibly NULL)

=item Crypt::OpenSSL::EC::EC_KEY::set_public_key($key, $pub);

Sets the public key of a EC_KEY object.
  key  EC_KEY object
  pub  EC_POINT object with the public key (note: the EC_KEY object
       will use an own copy of the EC_POINT object).
  return 1 on success and 0 if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::get_enc_flags($key);

=item Crypt::OpenSSL::EC::EC_KEY::set_enc_flags($key, $flags);

=item Crypt::OpenSSL::EC::EC_KEY::get_conv_form($key)

=item Crypt::OpenSSL::EC::EC_KEY::set_conv_form($key, $form);

=item Crypt::OpenSSL::EC::EC_KEY::get_key_method_data

Not Implemented

=item Crypt::OpenSSL::EC::EC_KEY::insert_key_method_data

Not Implemented

=item Crypt::OpenSSL::EC::EC_KEY::set_asn1_flag($key, $flag);


=item Crypt::OpenSSL::EC::EC_KEY::precompute_mult($key, $ctx);

Creates a table of pre-computed multiples of the generator to 
further EC_KEY operations.
  key  EC_KEY object
  ctx  BN_CTX object (optional)
  return 1 on success and 0 if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::generate_key($key);

Creates a new ec private (and optional a new public) key.
  key  EC_KEY object
  return 1 on success and 0 if an error occurred.

=item Crypt::OpenSSL::EC::EC_KEY::check_key($key);

Verifies that a private and/or public key is valid.
  key  the EC_KEY object
  return 1 on success and 0 otherwise.

=back


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2.1
- rebuild with new perl 5.22.0

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2
- to Sisyphus

* Thu Feb 05 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- regenerated from template by package builder

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.5-alt2
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- regenerated from template by package builder

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1
- initial import by package builder

