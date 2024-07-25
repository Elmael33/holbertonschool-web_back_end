import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  try {
    const results = await Promise.allSettled([
      signUpUser(firstName, lastName),
      uploadPhoto(fileName),
    ]);

    return results.map((result) => ({ status: 'fulfilled', value: result.value }));
  } catch (error) {
    console.error('Error handling profile signup:', error);
    return [];
  }
}
